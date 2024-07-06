# -*- coding: 1251 -*-
import os
import re

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    return len(sentences)

def main():
    folder_path = r'C:\Users\shekh\OneDrive\Рабочий стол\Дни практики\День 4\Задание 6'

    file_info = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                num_sentences = count_sentences(text)
                file_info[filename] = num_sentences

    sorted_file_info = dict(sorted(file_info.items(), key=lambda item: item[1]))

    for i, (filename, num_sentences) in enumerate(sorted_file_info.items(), start=1):
        new_filename = f"{num_sentences}_предложений.txt"
        new_file_path = os.path.join(folder_path, new_filename)
        old_file_path = os.path.join(folder_path, filename)
        os.rename(old_file_path, new_file_path)
        print(f"Файл {filename} переименован в {new_filename}")

    print("Готово! Файлы переименованы.")

if __name__ == "__main__":
    main()
