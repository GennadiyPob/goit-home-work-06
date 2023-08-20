file_list = ['file1.txt', 'file2.txt', 'file3.txt']  # Список файлів, які потрібно перемістити
destination_folder = 'destination_folder'  # Папка, куди потрібно перемістити файли

for file in file_list:
    source_path = file  # Шлях до вихідного файлу (в даному випадку в поточній директорії)
    destination_path = f"{destination_folder}/{file}"  # Шлях до папки призначення разом з іменем файлу
    shutil.move(source_path, destination_path)
    print(f"Файл '{file}' переміщено до папки '{destination_folder}'.")