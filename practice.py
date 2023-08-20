''' Прочитати перші `N` рядків текстового файлу. Ім'я файлу для читання передаємо як аргумент командного рядка'''

# import sys #підкючаємо бібліотеку sys для передачі в терміналі назви файлів

# NUM_LINES = 10 #вказуємо кількість рядків, які треба прочитати. 

# if len(sys.argv) !=2: #перевірка кількості параметрів для роботи. 
#     print('Not enought parameters')
#     quit()            #закінчення роботи програми 

# try:                  #використовуємо try except для відкриття файлу 
#     file = open(sys.argv[1], 'r', encoding='utf-8') #читаємо рядок
#     try:              
#         line = file.readline() #читаємо рядок
#         count = 0      #лічильник для руху по рядкам файлу
#         while count < NUM_LINES and line != '':
#             line = line.rstrip() #видаляємо пусті пробіли між рядками 
#             print(line)  #виводимо рядок 
#             count += 1 #перехід на інший рядок
#             line = file.readline()

#     except OSError:                        #Перевірка якщо файл не читається
#         print('Error while reading file')
#     finally:
#         file.close()       # Обов'язкове закриття файлу

# except OSError:                            #Перевірка якщо файл запаролений
#     print('Error with right for file') 


# import sys

# NUM_LINES = 10

# if len(sys.argv) !=2:
#     print('Not enought parameters')
#     quit()

# try:
#     with open(sys.argv[1], 'r', encoding='utf-8') as file:
#         lines = list()
#         for line in lines:
#             lines.append(line)
#             if len(line) > NUM_LINES:
#                 lines.pop(0)
#             for line in lines:
#                 print(line)

# except OSError:
#     print('Error with right for file') 

# import sys

# if len(sys.argv) == 1:
#     print('Set the file names as parameters in termanal')

# for i in range(1, len(sys.argv)):
#     file_name = sys.argv[i]  # індекс елементу в списку
#     try:
#         with open (file_name, 'r', encoding='utf-8') as file:
#             for line in file:
#                 print(line)
      
#     except OSError:
#         print('Error with right for file {file_name}') 

# NUM_LINES = 10

# if len(sys.argv) !=2:
#     print('Not enought parameters')
#     quit()

# try:
#     with open(sys.argv[1], 'r', encoding='utf-8') as file:
#         lines = list()
#         for line in lines:
#             lines.append(line)
#             if len(line) > NUM_LINES:
#                 lines.pop(0)
#             for line in lines:
#                 print(line)

# except OSError:
#     print('Error with right for file') 


'''Застосування Pathlib (файл автоматично закривається)'''

# from pathlib import Path

# NUM_LINES = 10

# if len(sys.argv) !=2:
#      print('Not enought parameters')
#      quit()



# file_name = Path('./Temp')
# try:
#     file = open(file_name/ 'jokes.txt', 'r', encoding='utf-8')
#     try:
#         while True:
#             line = file.readline()
#             if not line:


        
#     except OSError:
#         print('OSError') 

# except OSError:
#     print('OSError') 

'''Застосування glob - пошук файлів за патернами'''

# from pathlib import Path

# list_dir = Path('.')

# for elem in list_dir.glob('*.*'):   # glob('*.py*'), glob('*.txt')
#     print(elem)


'''Видаляємо файл'''

# from pathlib import Path

# try:
#     tmp = Path('C:/User')  #вказуємо шлях до файлу
#     tmp.unlink()           #стираємо файл

# except FileNotFoundError:
#     pass

'''Створення директорії'''

# from pathlib import Path

# new_dir = Path('tmp')
# # if not new_dir.exists(): #перевірка існування папки
# #     new_dir.mkdir()

# new_dir.mkdir(exist_ok=True) #перевірка існування папки

'''Створення директорії в директорії'''

# from pathlib import Path
# new_dir = Path('test/tmp') #створюємо папку test, а в ній папку tmp

# new_dir.mkdir(parents=True, exist_ok=True)

'''Переміщення файлів'''

# from pathlib import Path

# old_dir = Path('test.txt')
# new_dit = Path('Tmp/test.txt')

'''  Перезапис файла '''

# data = ['First line', 'Second line', 'Final line']

# folder = Path('Tmp')

# with open(folder/'data.txt', 'w', encoding='utf-8') as file:
#     for line in data:
#         file.wright('Temp')

'''  Кодування '''

# message = "Hello, Привіт, 你"

# print(message.encode())
# print(message.encode('utf_16'))
# print(message.encode('cp1251'))


# with open(folder/'utf_8.txt', 'wb') as f 

'''  Запис та зчитування інформації '''

# from pathlib import Path

# message = Path('test.txt')
# message.write_text('First line')
# message.write_text('Second line')

# #message.write_text('First line\nSecond line')

# print(message.read_text()) 

'''  Архіви '''

# import shutil

# archive = shutil.make_archive('bckup', 'zip', 'Temp/')
# print(archive)

# shutil.unpack_archive(archive, 'New_folder')


'''  Pillow виведення картинки що міститься в певній директорії '''

# from PIL import Image

# image = Image.open('tmp/python-logo.png')

# image.show()



