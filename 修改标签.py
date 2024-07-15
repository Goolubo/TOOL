import os
import re

def process_txt_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # 将int类型的“1”、“2”、“3”修改为“0”
    # content = re.sub(r'\b[1-3]\b', '0', content)
    content = re.sub(r'\b[4]\b', '1', content)


    # 将int类型的“6”、“7”修改为“5”
    # content = re.sub(r'\b[6-7]\b', '5', content)
    content = re.sub(r'\b[5]\b', '2', content)



    with open(file_path, 'w') as file:
        file.write(content)

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_txt_file(file_path)

# 指定文件夹路径
folder_path = "D:/桌面/新建文件夹"

# 处理文件夹中的所有txt文件
process_folder(folder_path)
