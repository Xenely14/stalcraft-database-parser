import requests
import asyncio
import redis
import time
import time
import bs4
import os

# Локальные импорты
from misc import *

# Константы, статические и глобальные переменные
REPOSITORY = "/EXBO-Studio/stalcraft-database"
RAW_URL = "https://raw.githubusercontent.com"
BASE_URL = "https://github.com"

SLEEP_TIME = 216000

database = redis.Redis(host="host", port="port", password="password", decode_responses=True)


async def parse():
    """Ф-ия парсер stalcraft-database"""

    while True:
        # Парсинг
        folders = list()

        repository = requests.get(BASE_URL + REPOSITORY)
        soup = bs4.BeautifulSoup(repository.content, "html.parser")

        repository = soup.find_all("a", {"class": "js-navigation-open Link--primary"})
        repository_hrefs = list(path["href"].replace("/blob/main/", "/main/") for path in repository)

        responses = await asyncio.gather(*[async_get(RAW_URL + url) for url in repository_hrefs])
        mset_dict = {":".join(repository_hrefs[index].replace(REPOSITORY, "")[1:].split("/")): responses[index].content for index in range(len(responses)) if responses[index].status_code == 200}
        database.mset(mset_dict) if mset_dict else None

        if mset_dict:

            for key in mset_dict.keys():
                print("Установлен ключ", end=" ")
                color_print("->", color="lightcyan_ex", end=" ")
                print(key)

        for response, url in zip(responses, repository_hrefs):

            if response.status_code == 404:
                folders.append(BASE_URL + url)

        while folders:
            repository = requests.get(folders[0])
            del folders[0]

            soup = bs4.BeautifulSoup(repository.content, "html.parser")

            repository = soup.find_all("a", {"class": "js-navigation-open Link--primary"})
            repository_hrefs = list(path["href"].replace("/blob/main/", "/main/") for path in repository)

            responses = await asyncio.gather(*[async_get(RAW_URL + url) for url in repository_hrefs])
            mset_dict = {":".join(repository_hrefs[index].replace(REPOSITORY, "")[1:].split("/")): responses[index].content for index in range(len(responses)) if responses[index].status_code == 200}
            database.mset(mset_dict) if mset_dict else None

            if mset_dict:

                for key in mset_dict.keys():
                    print("Установлен ключ", end=" ")
                    color_print("->", color="lightcyan_ex", end=" ")
                    print(key)

            for response, url in zip(responses, repository_hrefs):

                if response.status_code == 404:
                    folders.append(BASE_URL + url)

        # Ожидание повторного запуска
        color_print(f"Завершено, повторный запуск через: {SLEEP_TIME} секунд...", color="lightgreen_ex", end="\n")
        time.sleep(SLEEP_TIME)

# Запуск парсера
asyncio.run(parse())
