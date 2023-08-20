# import random
# ch = 1
# password = [] 
# def password_generator(password):
#     while ch < 8:
#         password += randint('A-Z', 'a-z', 0-9)


#     ch +=1
#     return password

# print(password_generator())



# new_name = "example"
# extension = ["txt"]
# print(new_name)
# print(extension)
# result = f'{new_name}.{".".join(extension)}'
# print(result)  # Виводить "example.txt"


from pathlib import Path

# parent_folder = Path('tmp') 

# new_folders = ['IMAGES', 'DOCUMENTS', 'AUDIO', 'VIDEO', 'ARCHIVES']


# for folder_name in new_folders:
#     folder_path = Path(parent_folder/folder_name)
#     if not folder_path.exists():
#         folder_path.mkdir()
#         print(f"Папка '{folder_name}' була створена.")
#     else:
#         print(f"Папка '{folder_name}' вже існує.")


folder_to_search = Path('tmp')  # Шлях до папки, в якій потрібно шукати пусті папки

for folder_path in folder_to_search.rglob('*'):
    if folder_path.is_dir() and not any(folder_path.iterdir()):  # Перевірка, чи папка порожня
        folder_path.rmdir()  # Видалення пустої папки
        print(f"Папку '{folder_path}' видалено.")