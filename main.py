import shutil
import sys
import scan
import normalize
from pathlib import Path
#from files_generator import file_generator

#обробка файлів. Path - збережений шлях до файлу: WindowsPath('tmp/Chess_position_from_black_side.jpg')
# root_folder - папка tmp
# dist - папка куди слід занести інформацію (перенести файли) 

def hande_file(path, root_folder, dist):                         
    target_folder = root_folder / dist                           #Директорія з адресою, куди слід занести інформацію 
    target_folder.mkdir(exist_ok=True)                           #Створення директорії, якщо вона не існує.  
    path.replace(target_folder/normalize.normalize(path.name))   #перенесення файлів в потрібну директорію з оновленням імені


def handle_archive(path, root_folder, dist):                     #обробка архівів
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.name.replace(".zip", ''))  #зміна імені файлової директорії, прибераємо розширення zip

    archive_folder = root_folder / new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(path.resolve()))  #розпаковка архівних файлів
    except shutil.ReadError:                                             #розпаковка архівних файлів
        archive_folder.rmdir()
        return
    except FileNotFoundError:                                            #розпаковка архівних файлів
        archive_folder.rmdir()
        return
    path.unlink()


def remove_empty_folders(path):                                          #видалення пустих папок
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
      

def main(folder_path):
    scan.scan(folder_path)
    remove_empty_folders(folder_path) 
    
    for file in scan.jpeg_files:                    # проходимо по списку файлів зображень
        hande_file(file, folder_path, "IMAGES")     # записуємо file за адресою folder_path в папку IMAGES

    for file in scan.doc_files:
        hande_file(file, folder_path, "DOCUMENTS")

    for file in scan.video_files:
        hande_file(file, folder_path, "VIDEO")

    for file in scan.music_files:
        hande_file(file, folder_path, "AUDIO")

    for file in scan.archives:
        handle_archive(file, folder_path, "ARCHIVES")
    
       
    get_folder_objects(folder_path)


path = sys.argv[1]                                    #запуск через термінал, [1] - ім'я директорії 
arg = Path(path)   

main(arg.resolve())

