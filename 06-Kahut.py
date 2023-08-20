'''01'''
# fh = open('example.txt') № fh - файловий дескриптор і змінна. Покажчик файлів.

'''02'''
# fh = open('example.txt') № відкриття файлу. Друга позиція за умовчанням 'r' на читання (read).

'''03'''
# fh = open('example.txt')
# fh.write('Hello')
# fh.close()

#Код викличе помилку, бо не вказана команда на запис у файл 'w'

'''04'''
# fh = open('example.txt', 'w')
# print(fh.write('Hello'))
# fh.close()

#Код записує в файл слово 'Hello', а в консоль виводить '5' - кількість букв в слові Hello, як кількість символів для запису.

'''05'''
# fh = open('example.txt', 'x')
# fh.write('world!')
# fh.close()

#Буде помилка, оскільки 'x' - означає створення файлу, а файл вже існує.

'''06'''
# Вміст файлу 'example.txt':
# Hello

# fh = open('example.txt', 'r')
# data = fh.read(3)
# print(data)
# fh.close()

#В консоль виведе перші ТРИ букви : Hel 

'''07'''
# Вміст файлу 'example.txt':
# Hello

# fh = open('example.txt', 'r')
# fh.seek(2)                      #seek пропускає перші ДВА символи
# data = fh.read(3)
# print(data)
# fh.close()

# Пропустить перші два вимволи і прочитає наступні ТРИ : llo

'''08'''
# Вміст файлу 'example.txt':
# Hello

# fh = open('example.txt', 'r')
# for el in range (1,6):
#     data = fh.read(1)
#     print(data)
# fh.close()

#В консоль виведе всі букви Hello по одній в кожному рядку

'''09'''
# Вміст файлу 'example.txt':
# Hello

# with open('example.txt', 'a') as fh:   # 'a' - дозапис у файл
#     data = fh.write(' world!')
#     print(data)
    

#В файлі буде: 'Hello world!', а в консоль виведе 7 - кількість символів ' world!'

'''10'''
# Вміст файлу 'example.txt':
# Hello

# with open('example.txt', 'w') as fh:     # 'w' - дозапис у файл
#     data = fh.write(' world!')
#     print(data)
    

#В файлі буде ' world!', бо запис йде поверх існуючого тексту. В консолі виведе 7 - кількість символів ' world!'

'''11'''
# message = b'Hello'     # b - бінарна строка
# print(message[1:3])    # команда виводить 1-й і 2-й символ, але перед ними буде b. 

# В консолі буде b'el'

'''12'''
# message = b'Hello'     # b - бінарна строка
# msg = 'Hello'
# print(message == msg.encode())    # encode - переведення в бінарний вигляд 

# В консолі буде True

'''13'''
# message = b'Hello'     # b - бінарна строка
# msg = 'Hello'
# print(message == msg)     

# В консолі буде False

