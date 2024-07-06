# -*- coding: 1251 -*-
import os
import time

def find_largest_file(folder_path):
    largest_size = 0
    largest_file = None

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size > largest_size:
                largest_size = file_size
                largest_file = filename

    return largest_file

def main():
    folder_path = r'C:\Users\shekh\OneDrive\Рабочий стол\Дни практики\День 4\Задание 8'  

    largest_filename = find_largest_file(folder_path)
    if largest_filename:
        largest_file_path = os.path.join(folder_path, largest_filename)
        largest_file_size = os.path.getsize(largest_file_path)
        creation_time = os.path.getctime(largest_file_path)

        formatted_creation_time = time.strftime("%d_%m_%Y", time.localtime(creation_time))

        file_extension = os.path.splitext(largest_filename)[1].lstrip('.')

        new_filename = f"{file_extension}_{formatted_creation_time}.{file_extension}"
        new_file_path = os.path.join(folder_path, new_filename)


        os.rename(largest_file_path, new_file_path)
        print(f"Файл {largest_filename} переименован в {new_filename}")
    else:
        print("В указанном каталоге нет файлов.")

if __name__ == "__main__":
    main()
