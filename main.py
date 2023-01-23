import requests
import asyncio
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

SLEEP_TIME = 72000


async def parse():

    while True:

        # Парсинг
        folders = list()

        repository = requests.get(BASE_URL + REPOSITORY)
        soup = bs4.BeautifulSoup(repository.content, "html.parser")

        repository = soup.find_all("a", {"class": "js-navigation-open Link--primary"})
        repository_hrefs = list(path["href"].replace("/blob/main/", "/main/") for path in repository)

        # Создание корневой папки
        if not os.path.exists("main"):
            os.mkdir("main")

        responses = await asyncio.gather(*[async_get(RAW_URL + url) for url in repository_hrefs])

        for response, url in zip(responses, repository_hrefs):

            if response.status_code == 404:
                path = url.replace(REPOSITORY, "").replace("/tree/main", "")

                if not os.path.exists("main" + path):
                    os.mkdir("main" + path)

                color_print("Получен путь", color="lightblack_ex", end=" ")
                color_print("->", color="lightcyan_ex", end=" ")
                print(f"{BASE_URL}{url}", end="\n")
                folders.append(BASE_URL + url)

            else:
                file = url.replace(REPOSITORY, "")

                if file.endswith(".png"):
                    with open(file[1:], "wb") as file:
                        file.write(response.content)

                else:
                    with open(file[1:], "w", encoding="utf-8") as file:
                        file.write(response.content.decode(encoding="utf-8"))

                print("Получен файл", end=" ")
                color_print("->", color="lightcyan_ex", end=" ")
                print(f"{RAW_URL}{url}", end="\n")

        while folders:

            repository = requests.get(folders[0])
            del folders[0]

            soup = bs4.BeautifulSoup(repository.content, "html.parser")

            repository = soup.find_all("a", {"class": "js-navigation-open Link--primary"})
            repository_hrefs = list(path["href"].replace("/blob/main/", "/main/") for path in repository)

            responses = await asyncio.gather(*[async_get(RAW_URL + url) for url in repository_hrefs])

            for response, url in zip(responses, repository_hrefs):

                if response.status_code == 404:
                    path = url.replace(REPOSITORY, "").replace("/tree/main", "")

                    if not os.path.exists("main" + path):
                        os.mkdir("main" + path)

                    color_print("Получен путь", color="lightblack_ex", end=" ")
                    color_print("->", color="lightcyan_ex", end=" ")
                    print(f"{BASE_URL}{url}", end="\n")
                    folders.append(BASE_URL + url)

                else:
                    file = url.replace(REPOSITORY, "")

                    if file.endswith(".png"):
                        with open(file[1:], "wb") as file:
                            file.write(response.content)

                    else:
                        with open(file[1:], "w", encoding="utf-8") as file:
                            file.write(response.content.decode(encoding="utf-8"))

                    print("Получен файл", end=" ")
                    color_print("->", color="lightcyan_ex", end=" ")
                    print(f"{RAW_URL}{url}", end="\n")

        # Ожидание повторного запуска
        color_print(f"Дамп сделан! Повторный запуск через: {SLEEP_TIME} секунд...", color="lightgreen_ex", end="\n")
        time.sleep(SLEEP_TIME)

# Запуск парсера
asyncio.run(parse())
