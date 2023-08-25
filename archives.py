import sys
import shutil
import zipfile
import normalize
from pathlib import Path

def move_and_extract_file(file_path, target_folder):
    file_path = Path(file_path)
    target_folder = Path(target_folder)
    
    if not file_path.exists() or not file_path.is_file():
        print("Файл не існує.")
        return
    
    if not target_folder.exists() or not target_folder.is_dir():
        print("Цільова папка не існує.")
        return
    
    # Переміщення файлу в папку "Archives"
    new_file_path = target_folder / file_path.name
    shutil.move(file_path, new_file_path)
    
    # Розпакування файлу (якщо це ZIP-архів)
    if new_file_path.suffix.lower() == ".zip":
        with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
            zip_ref.extractall(target_folder)
            print(f"Файл '{new_file_path.name}' розпаковано в '{target_folder}'.")
    else:
        print(f"Файл '{new_file_path.name}' переміщено в '{target_folder}', але не розпаковано.")

# Виклик функції для переміщення та розпакування файлу
file_path = 'tmp/textї.txt.zip'
target_folder = 'tmp/ARCHIVES'

move_and_extract_file(file_path, target_folder)
#У цьому коді функція move_and_extract_file приймає шлях до файлу (file_path) та шлях до цільової папки (target_folder). Код спершу переміщує файл в папку "Archives" за допомогою shutil.move, а потім перевіряє розширення файлу, щоб визначити, чи це ZIP-архів. Якщо це ZIP-архів, він розпаковує його за допомогою zipfile.ZipFile.


path = sys.argv[1]                                    #запуск через термінал
arg = Path(path)




