# -*- coding: 1251 -*-
import os
import glob
import shutil
from datetime import datetime

source_folder = r'C:\Users\shekh\OneDrive\Рабочий стол\Дни практики\День 4\Задание 7'

files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]


files.sort(key=lambda x: os.path.getctime(os.path.join(source_folder, x)))

for filename in files:
    file_path = os.path.join(source_folder, filename)
    creation_time = os.path.getctime(file_path)
    month_name = datetime.fromtimestamp(creation_time).strftime("%B").lower()
    month_folder = os.path.join(source_folder, month_name)

    if not os.path.exists(month_folder):
        os.makedirs(month_folder)

    shutil.move(file_path, os.path.join(month_folder, filename))

print("Файлы успешно отсортированы по месяцам!")
