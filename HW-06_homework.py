'''Task 1. Читаємо файл. Складаємо суму зарплат працівників'''

# def total_salary(path):
#     summary = 0 
#     file = open(path, 'r', encoding='utf-8')

#     try:
#         line = file.readline()
#         while line != '':
#             line = line.rstrip()
#             salary = line.split(',')[-1]
#             summary += float(salary)
#             line = file.readline()

#     except OSError:
#         print('Error while reading file')
#     finally:
#         file.close()
#     return summary



'''Task 2. Запис працівників в файл'''

# def write_employees_to_file(employee_list, path):
#     file = open(path, 'w')          # 'w' - wright відкриття на запис, вміст файлу видаляється, якщо файлу не існує, створюється новий.
    
#     for department in employee_list:
#         for employee in department:
#             file.write(employee + '\n')  # 'w' - запис. кожний рядок з нової строки.
    
#     file.close()  #закриття файлу

# # Виклик функції
# employees = [
#     ['Robert Stivenson,28', 'Alex Denver,30'],
#     ['Drake Mikelsson,19']
# ]
# write_employees_to_file(employees, 'employees.txt')

'''Task 3. зчитування переліку працівників. Формування списку'''

# def read_employees_from_file(path):
#     employee_list = []
#     file = open(path, 'r', encoding='utf-8')

#     try:
#         line = file.readline()
#         while line != '':
#             line = line.rstrip()
#             employee_list.append(line.strip())
#             line = file.readline()

#     except OSError:
#         print('Error while reading file')
#     finally:
#         file.close()
#     return employee_list

'''Task 4. Дозапис інформації в файл '''

# def add_employee_to_file(record, path):
    
#     file = open(path, 'a')          # 'w' - wright відкриття на запис, вміст файлу видаляється, якщо файлу не існує, створюється новий.
    
#     record = 'Drake Mikelsson,19'
    
#     file.write(record + '\n')  # 'w' - запис. кожний рядок з нової строки.
    
#     file.close()  #закриття файлу

'''Task 5. Autochek. Дозапис інформації в файл '''

# from pathlib import Path

# #info_path = Path('.cats_info.txt')

# def get_cats_info(path):
    
#     result = []  
#     with open(path, "r") as f:  
#         for string in f:  
#             id, name, age = string.split(",")  
#             result.append({"id": id, "name": name, "age": age.strip()})  
#     return result
    
'''Task 6. Autochek. Пошук рецепту'''

# def get_recipe(path, search_id):
#     with open(path, 'r') as file:
#         for line in file:
#             if search_id in line:
#                 data = line.replace('\n', '').split(',')
#                 return {'id': data[0], 'name': data[1], 'ingredients': data[2:]}
   


'''Task 7. Autochek. Зчитати інфо з файлу. Видалити цифри. Записати в новий файл'''
# def sanitize_file(source, output):
#     try:
#         with open(source, 'r') as file:
#             readed_text = file.read()
#             text_without_digits = ''.join([char for char in readed_text if not char.isdigit()])
        
#         with open(output, 'w') as output:
#             output.write(text_without_digits)
        
#         print("Текст без цифр записано :", output)
    
#     except FileNotFoundError:
#         print("Файл не знайдеyний")  

# # Використання функції
# source_file_name = "input.txt"  # Замініть на ім'я вхідного файлу
# output_file_name = "output.txt"  # Замініть на ім'я вихідного файлу
# sanitize_file(source_file_name, output_file_name)


'''Task 7. Autochek. Зчитати інфо з файлу. Видалити цифри. Записати в новий файл (варіант лектора)'''
# import re
# def sanitize_file(source, output):
#     text = None
#     with open(source, 'r') as file:
#         text = file.readline()

#     text = re.sub(r'\d', '', text)

#     with open(output, 'w') as output:
#         file.write(text)


'''Task 8. ОБробити Зчитати інфо з файлу. Видалити цифри. Записати в новий файл'''
# def save_applicant_data(source, output):
#     with open(output, 'w') as output_file:
#         for applicant in source:
#             data_line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
#             print(data_line)
#             output_file.write(data_line)

# # Приклад використання функції
# applicant_data = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]

# output_file_name = "applicant_data.txt"
# save_applicant_data(applicant_data, output_file_name)

'''Task 9. '''

# def is_equal_string(utf8_string, utf16_string):
#     return utf8_string.decode() == utf16_string.decode('utf-16')

'''Task 10. Функція запису логіну і паролю у файл у бінарному вигляді '''

# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as file:
#         for username, password in users_info.items():
#             result = f'{username}:{password}'
#             file.write(f'{result}\n'.encode('utf-8'))


'''Task 11. Функція повертає рядок з бінарного файлу '''

# def get_credentials_users(path):
#     output = list()
#     with open (path, 'rb') as file:
#         for line in file:
#             data = line.decode().replace('\n', '')
#     return output

'''Task 12. Кодування у BASE64 '''

# import base64

# def encode_data_to_base64(data):
#     output = list()
#     for elem in data:
#         message_bytes = elem.encode('utf-8')
#         base64_bytes = base64.b64encode(message_bytes)
#         base64_message = base64_bytes.decode('utf-8')
#         output.append(base64_message)
#     return output

'''Task 13. Архівування '''

# import shutil

# def create_backup(path, file_name, employee_residence):
#     with open(f'{path}/{file_name}', 'wb') as file:
#         for employee, residence in employee_residence.items():
#             line = f'{employee} {residence}\n'
#             file.write(line.encode())
#         shutil.make_archive(f'backup_folder', 'zip', path)
#         return f'{path}/backup_folder.zip'


'''Task 14. Розпакування архіву '''

# import shutil

# def unpack(archive_path, path_to_unpack):
#     shutil.unpack_archive(archive_path, path_to_unpack)