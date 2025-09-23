import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def show_folder(path, level=0):
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        indent = "  " * level  # делаем отступы
        if os.path.isdir(full_path):
            print(Fore.BLUE + f"{indent}{name}")
            show_folder(full_path, level + 1)
        else:
            print(Fore.GREEN + f"{indent}{name}")

if len(sys.argv)<2:
    print('Шлях не вказаний')
    sys.exit(1)

folder_path = sys.argv[1]
if not os.path.exists(folder_path):
    print('Шлях не знайдений')
    sys.exit(1)
if not os.path.isdir(folder_path):
    print('Шлях веде не до папки')
    sys.exit(1)

show_folder(folder_path)
