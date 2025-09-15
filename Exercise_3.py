import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)  # сбрасывать цвет после каждой строки

# Проверяем, передан ли аргумент
if len(sys.argv) < 2:
    print("Пожалуйста, укажите путь к директории.")
    sys.exit(1)

path = Path(sys.argv[1])

# Проверка, существует ли путь и это директория
if not path.exists():
    print("Такого пути не существует!")
    sys.exit(1)
if not path.is_dir():
    print("Указанный путь не ведет к директории!")
    sys.exit(1)

# Простейший вывод содержимого папки
for item in path.iterdir():
    if item.is_dir():
        print(Fore.BLUE + f"[DIR] {item.name}")
    else:
        print(Fore.GREEN + f"[FILE] {item.name}")
