import colorama
import requests
import asyncio

colorama.init(autoreset=True)


def async_get(url: str) -> None:
    """Возвращает Future c request.get запросом для дальнейшей обработки в gather'e"""

    return asyncio.get_event_loop().run_in_executor(None, requests.get, url)


def color_print(output: str, color: str, end: str = "\n") -> None:
    """Выводит цветной текст в консоль"""

    exec(f"print(colorama.Fore.{color.upper()} + output, end=end)")
