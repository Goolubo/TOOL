
import os
import shutil

# 文件夹1、文件夹2和文件夹3的路径:将文件夹2中和文件夹1中同名的文件移动到文件夹3中
folder1 = 'D:/Study/ultralytics-main/datasets/road2020-seg/images/val2020'
folder2 = 'D:/jsai/turn0255/black_images_txt'
folder3 = 'D:/Study/ultralytics-main/datasets/road2020-seg/labels/val2020'

# 获取文件夹1中的文件列表
folder1_files = os.listdir(folder1)

# 获取文件夹2中的文件列表
folder2_files = os.listdir(folder2)

# 确保文件夹3存在
if not os.path.exists(folder3):
    os.makedirs(folder3)

# 遍历文件夹1中的文件
for file1 in folder1_files:
    base_name, ext = os.path.splitext(file1)

    # 检查是否存在同名但后缀为.txt的文件在文件夹2中
    txt_file2 = base_name + '.txt'

    if txt_file2 in folder2_files:
        # 构建文件的完整路径
        source_path = os.path.join(folder2, txt_file2)
        target_path = os.path.join(folder3, txt_file2)

        # 将文件从文件夹2移动到文件夹3
        shutil.move(source_path, target_path)

print("Files moved to folder3.")



