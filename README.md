# stalcraft-database-parser
Полуасинхронный парсер stalcraft-database

### Примечание
Работает посредством HTTP-запросов на github репозиторий "stalcraft-database":  https://github.com/EXBO-Studio/stalcraft-database.<br/>
Используемые сторонние пакеты: colorama, requests, bs4.<br/>
Версия Python: ^=3.7<br/>

### Запуск и испльзование
Windows:
1. Установить Python
2. Установить нужные пакеты при помощи команды в терменале: ```pip install colorama requests bs4```
3. Поместить файл "main.py" и "misc.py" в одну папку
4. Запустить файл "main.py" при помощи команды в терминале: ```python main.py```

Linux:
1. Установить нужные пакеты при помощи команды в терменале: ```pip3 install colorama requests bs4```
2. Поместить файл "main.py" и "misc.py" в одну папку3
3. Запустить файл "main.py" при помощи команды в терминале: ```python3 main.py```

P.S. Для постоянной работы скрипта используйте утилиту screen:</br>
https://gist.github.com/drewlesueur/950187/1e3382cbcd1ef012c68487fbc2e38c8963fc3b3c

![изображение](https://user-images.githubusercontent.com/83385888/213999777-632a20da-b408-4708-b097-1b535a8b02b1.png)

### Важно
По умолчанию скрипт срабатывает каждые 2 часа (7200 сек). Данный показатель можно изменить на 16 строке файла "main.py":
![изображение](https://user-images.githubusercontent.com/83385888/214000182-3164521f-abf2-408e-8a45-7d8d59af806f.png)

После успешной работы скрипта будет создана папка "main", содержащая в себе все содержимое репозитория:
![изображение](https://user-images.githubusercontent.com/83385888/214000546-3c68f1e1-4845-4180-9e9e-943cd2438eb0.png)
![изображение](https://user-images.githubusercontent.com/83385888/214000589-3e6e5b3a-50ad-4283-969f-7464ee64fae1.png)

Время дампинга: ~3-6 минуты (зависит от скорости соединения, ЦП и ОЗУ)

