import os
import random
import shutil

# 源文件夹和目标文件夹的路径
source_folder = 'D:/jsai/FinalData2/data2jpg'
target_folder = 'D:/Study/ultralytics-main/datasets/road2020-seg/images/val2020'

# 获取源文件夹中的所有文件
all_files = os.listdir(source_folder)

# 如果文件夹中文件数量小于400，可以选择全部文件
if len(all_files) <= 400:
    files_to_move = all_files
else:
    # 随机选择400个文件
    files_to_move = random.sample(all_files, 400)

# 确保目标文件夹存在
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 移动文件
for file_name in files_to_move:
    source_path = os.path.join(source_folder, file_name)
    target_path = os.path.join(target_folder, file_name)
    shutil.move(source_path, target_path)

print(f"Moved {len(files_to_move)} files from {source_folder} to {target_folder}")
