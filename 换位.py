# 将文件夹中所有txt文件和jpg文件转移到另一个文件夹中

import os
import shutil

# 源文件夹路径
source_folder = 'D:/Study/pycharm_project/Tool'

# 目标文件夹路径
destination_folder = 'D:/jsai/FinalData2/jpg8'

# 获取源文件夹中的所有.txt和.jpg文件
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # if file.endswith('.txt') or file.endswith('.jpg'):
        if file.endswith('.jpg'):
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)

            # 移动文件
            # shutil.copy(source_file, destination_file)
            shutil.move(source_file, destination_file)
            print(f'Moved: {source_file} -> {destination_file}')
