import os

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()

def compare_text_files_in_directories(dir1, dir2):
    files1 = {file for file in os.listdir(dir1) if file.endswith('.txt')}
    files2 = {file for file in os.listdir(dir2) if file.endswith('.txt')}

    same_files_diff_content = []
    for file in files1.intersection(files2):
        file1 = os.path.join(dir1, file)
        file2 = os.path.join(dir2, file)
        if not compare_files(file1, file2):
            same_files_diff_content.append(file)

    return same_files_diff_content

# 替换这些路径为您的文件夹路径
dir1 = "D:/桌面/label_0.261"
dir2 = "D:/桌面/labels_11.19"

# 运行比较
different_files = compare_text_files_in_directories(dir1, dir2)
print("以下文件在两个文件夹中内容不同:", different_files)
