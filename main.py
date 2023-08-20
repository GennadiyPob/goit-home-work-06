import shutil
import sys
import scan
import normalize
from pathlib import Path
#from files_generator import file_generator


def hande_file(path, root_folder, dist):                         #обробка файлів
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))   #оновлення імені файлів


def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.name.replace(".zip", ''))

    archive_folder = root_folder / new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(path.resolve()))  #розпаковка архівних файлів
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()


def remove_empty_folders(path):    #видалення пустих папок
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass



def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass

# folder_to_search = Path('root_folder')  # Шлях до папки, де слід шукати пусті папки

# for folder_path in folder_to_search.rglob('*'):
#     if folder_path.is_dir() and not any(folder_path.iterdir()):  # Перевірка, чи папка порожня
#         folder_path.rmdir()  # Видалення пустої папки
      

def main(folder_path):
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        hande_file(file, folder_path, "IMAGES")

    for file in scan.doc_files:
        hande_file(file, folder_path, "DOCUMENTS")

    for file in scan.video_files:
        hande_file(file, folder_path, "VIDEO")

    for file in scan.music_files:
        hande_file(file, folder_path, "AUDIO")

    for file in scan.archives:
        handle_archive(file, folder_path, "ARCHIVES")

    get_folder_objects(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")
    
    arg = Path(path)
    main(arg)




