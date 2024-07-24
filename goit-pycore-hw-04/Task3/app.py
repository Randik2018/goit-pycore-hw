import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(path, indent = ''):
    if path.is_dir():
        print(f"{indent}{Fore.BLUE}{path.name}{Style.RESET_ALL}")
        indent += '    '
        for item in path.iterdir():
            if item.is_dir():
                print_directory_structure(item, indent)
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


if len(sys.argv) != 2:
        print("Використайте: python app.py <directory_path>")
        sys.exit(1)
directory_path = Path(sys.argv[1])
if not directory_path.is_dir():
    print(f"{Fore.RED}Наданий шлях не є каталогом або не існує.{Style.RESET_ALL}")
    sys.exit(1)
print_directory_structure(directory_path)