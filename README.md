# stalcraft-database-parser
Полуасинхронный парсер stalcraft-database

### Примечание
Работает посредством HTTP-запросов на github репозиторий "stalcraft-database":  https://github.com/EXBO-Studio/stalcraft-database.<br/>
Используемые сторонние пакеты: colorama, requests, bs4, redis. </br>
Версия Python: ^=3.7<br/>

# 1. semisasync

### Запуск и испльзование

filecollector.py - создает каталог с файлами перозирония </br>
rediscollector.py - переносит содержимое репозитория в Redis базу данных </br>

Windows:
1. Установить Python
2. Установить нужные пакеты при помощи команды в терменале: ```pip install colorama requests bs4 redis```
3. Поместить файл "filecollector.py", "rediscollector.py" и "misc.py" в одну папку
4. Запустить нужный вам файл при помощи команды в терминале: ```python <filename.py>```

Linux:
1. Установить нужные пакеты при помощи команды в терменале: ```pip3 install colorama requests bs4 redis```
2. Поместить файл "main.py" и "misc.py" в одну папку3
3. Запустить файл "main.py" при помощи команды в терминале: ```python <filename.py>```

P.S. Для постоянной работы скрипта используйте утилиту screen:</br>
https://gist.github.com/drewlesueur/950187/1e3382cbcd1ef012c68487fbc2e38c8963fc3b3c

filecollector.py: </br>
![изображение](https://user-images.githubusercontent.com/83385888/213999777-632a20da-b408-4708-b097-1b535a8b02b1.png)

rediscollector.py: </br>
![изображение](https://user-images.githubusercontent.com/83385888/214212210-62fa88f5-0fe1-46cd-9859-889d2c87555b.png)

### Важно
По умолчанию скрипты срабатывает каждые 2 часа (7200 сек). Данный показатель можно изменить на 16 и 17 строке файлов:
![изображение](https://user-images.githubusercontent.com/83385888/214000182-3164521f-abf2-408e-8a45-7d8d59af806f.png)
![изображение](https://user-images.githubusercontent.com/83385888/214210598-f6d868c5-1c80-4f07-848d-1fb0d93fb121.png)


После успешной работы "filecollector.py" будет создана папка "main", содержащая в себе все содержимое репозитория:
![изображение](https://user-images.githubusercontent.com/83385888/214000546-3c68f1e1-4845-4180-9e9e-943cd2438eb0.png)
![изображение](https://user-images.githubusercontent.com/83385888/214000589-3e6e5b3a-50ad-4283-969f-7464ee64fae1.png)

Для успешного подключения к базе данных необходимо изменить её хост, порт и пароль на 19 строке файла "rediscollector.py":
![изображение](https://user-images.githubusercontent.com/83385888/214211576-ca1b118d-47d5-4b4e-957e-1d7cb5ac1d96.png)

После успешной работы "rediscollector.py" база данных будет содержать в себе содержимое репозитория: 
![изображение](https://user-images.githubusercontent.com/83385888/214212393-ce593510-dcc3-47fa-9f75-8aa06b7b6f14.png)

Время полного парсинга: ~3-6 минуты (зависит от скорости соединения, ЦП и ОЗУ)

