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
    return Path(file_name).suffix[1:].upper()   #працюємо з суфіксом (беремо розширення) файлу  

'''сканування папок'''
def scan(folder):
    for item in folder.iterdir():                #проходимо по всім елементам папки
        if item.is_dir():                        #перевірка чи є елемент папцкою
            if item.name not in ('IMAGES' , 'DOCUMENTS', 'AUDIO', 'VIDEO', 'ARCHIVES'):  #ігноруємо папки для відсортованих файлів
                folders.append(item)             #додаємо назву пройденого каталогу в список
                scan(item)                       #скануємо папку                   
            continue                             #якщо папка зі списку то пропускаємо її

        #блок роботи з файлами  
        extension = get_extensions(file_name=item.name)  #працюємо з розширенням (відділяємо)

        new_name = folder / item.name                    #new_name - шлях. Передаємо шлях до файлу  

        if not extension:                                #перевіряємо чи є у файла розширення
            others.append(new_name)                      #додаємо його в список 'OTHERS'
        
        else:                                            #працюємо з файлами з розширеннями
            try:
                container = registered_extensions[extension]
                extensions.add(extension)                 #зберігаємо відомі розширення в множину (set)
                container.append(new_name)                #додаємо в контейнер ім'я файлу
            except KeyError:                              #KeyError якщо розширення не знайдено  
                unknown.add(extension)                    #зберігаємо НЕвідомі розширення
                others.append(new_name)                   #зберігаємо файли без розширень


# if __name__ == '__main__':
#     path = sys.argv[1]                                    #запуск через термінал
#     print(f'Start in {path}')

#     arg = Path(path)                                      #Отримання шляху до файлу у вигляді аргумента. 
    
#     scan(arg)


    #друкуємо те що зберегли в контейнерах
    print(f'IMAGES jpeg, jpg, png, svg: {jpeg_files}\n')    
    print(f'VIDEO mp4, avi, mov, mkv : {video_files}\n')
    print(f'DOCS docs, doc, txt, xlsx, pptx, pdf : {doc_files}\n')
    print(f'MUSIC mp3, ogg, wav, amr: {music_files}\n')
    print(f'ARCHIVES zip, gz, rar: {archives}\n')
    print(f'others: {others}\n')
    print(f'All extensions: {extensions}')
    print(f'unknown extentions: {unknown}\n')

 
'''Створення папок''' 

# parent_folder = Path(sys.argv[1]) 

# new_folders = ['IMAGES', 'DOCUMENTS', 'AUDIO', 'VIDEO', 'ARCHIVES']


# for folder_name in new_folders:
#     folder_path = Path(parent_folder / folder_name)
#     if not folder_path.exists():
#         folder_path.mkdir()
#         print(f"Папка '{folder_name}' створена.")
#     else:
#         print(f"Папка '{folder_name}' вже існує.")


'''Сортування файлів по папкам''' 

# for file in jpeg_files:
#     shutil.move(file, 'IMAGES')

# for file in doc_files:
#     shutil.move(file, 'DOCUMENTS')

# for file in music_files:
#     shutil.move(file, 'AUDIO')

# for file in video_files:
#     shutil.move(file, 'VIDEO')

# for file in archives:
#     shutil.move(file, 'ARCHIVES')



