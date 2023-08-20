'''Функція сканування папок'''

import sys
import shutil
from pathlib import Path #Path для ітерування (проходження) по файлам і папкам

'''створюємо списки відповідно до розширення файлів'''
jpeg_files = list()
doc_files = list()
video_files = list()
music_files = list()
folders = list()
archives = list()
others = list()
unknown = set()           #колекція НЕвідомих розширень  
extensions = set()        #колекція відомих розширень  

#словник, в якому ключі - розширення файлів
registered_extensions = {
    "JPEG": jpeg_files,
    "PNG": jpeg_files,
    "JPG": jpeg_files,
    "SVG": jpeg_files,
    "TXT": doc_files,
    "DOCX": doc_files,
    "DOC": doc_files,
    "XLSX": doc_files,
    "PPTX": doc_files,
    "PDF": doc_files,
    "AVI": video_files,
    "MP4": video_files,
    "MOV": video_files,
    "MKV": video_files,
    "MP3": music_files,
    "OGG": music_files,
    "WAV": music_files,
    "AMR": music_files,
    "ZIP": archives,
    "GZ": archives,
    "RAR": archives,
    "TAR": archives
}

#ф-ція обробки розширень
def get_extensions(file_name):                  #отримуємо ім'я файлу
    return Path(file_name).suffix[1:].upper()   #працюємо з суфіксом (розширенням) файлу  

'''сканування папок'''
def scan(folder):
    for item in folder.iterdir():                #проходимо по файлам папки
        if item.is_dir():                        #перевірка чи ми в папці
            if item.name not in ('IMAGES' , 'DOCUMENTS', 'AUDIO', 'VIDEO', 'ARCHIVES'):  #ігноруємо папки для відсортованих файлів
                folders.append(item)             #додаємо назву пройденого каталогу в список
                scan(item)                       #скануємо папку                   
            continue

        #блок роботи з файлами  
        extension = get_extensions(file_name=item.name)  #працюємо з розширенням
        new_name = folder/item.name                      #передаємо шлях до файлу  

        if not extension:                                #працюємо з файлами без розширення
            others.append(new_name)                      #Додаємо в список 'OTHERS'
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)                 #зберігаємо відомі розширення
                container.append(new_name)
            except KeyError:
                unknown.add(extension)                    #зберігаємо НЕвідомі розширення
                others.append(new_name)                   #зберігаємо файла з НЕвідомим розширенням

if __name__ == '__main__':
    path = sys.argv[1]                                    #запуск через термінал
    print(f'Start in {path}')

    arg = Path(path)                                      #Отримання шляху до файлу у вигляді аргумента. 
    
    scan(arg)

    print(f'IMAGES jpeg, jpg, png, svg: {jpeg_files}\n')
    print(f'VIDEO mp4, avi, mov, mkv : {video_files}\n')
    print(f'DOCS docs, doc, txt, xlsx, pptx, pdf : {doc_files}\n')
    print(f'MUSIC mp3, ogg, wav, amr: {music_files}\n')
    print(f'ARCHIVES zip, gz, rar: {archives}\n')
    print(f'others: {others}\n')
    print(f'All extensions: {extensions}')
    print(f'unknown extentions: {unknown}\n')


'''Створення папок''' 

parent_folder = path

new_folders = ['IMAGES', 'DOCUMENTS', 'AUDIO', 'VIDEO', 'ARCHIVES']


for folder_name in new_folders:
    folder_path = Path(parent_folder / folder_name)
    if not folder_path.exists():
        folder_path.mkdir()
        print(f"Папка '{folder_name}' створена.")
    else:
        print(f"Папка '{folder_name}' вже існує.")


'''Сортування файлів по папкам''' 

for file in jpeg_files:
    shutil.move(file, 'IMAGES')

for file in doc_files:
    shutil.move(file, 'DOCUMENTS')

for file in music_files:
    shutil.move(file, 'AUDIO')

for file in video_files:
    shutil.move(file, 'VIDEO')

for file in archives:
    shutil.move(file, 'ARCHIVES')
















