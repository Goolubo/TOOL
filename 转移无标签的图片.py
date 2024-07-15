import os
import shutil

def move_unmatched_jpg_files(src_dir, dest_dir):
    # 确保目标文件夹存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(src_dir):
        if filename.endswith('.jpg'):
            jpg_file = os.path.splitext(filename)[0]
            json_file = jpg_file + '.json'
            jpg_path = os.path.join(src_dir, filename)
            json_path = os.path.join(src_dir, json_file)

            # 如果没有与jpg文件同名的json文件，则移动jpg文件
            if not os.path.exists(json_path):
                shutil.move(jpg_path, os.path.join(dest_dir, filename))
                print(f"Moved: {jpg_path} -> {os.path.join(dest_dir, filename)}")

# 示例用法
source_folder = 'D:/图片/bricycle2-6.19'  # 替换为实际的源文件夹路径
destination_folder = 'D:/图片/bricycle2-6.19-no-json'  # 替换为实际的目标文件夹路径

move_unmatched_jpg_files(source_folder, destination_folder)
