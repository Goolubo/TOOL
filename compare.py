import os

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def compare_folders(folder1, folder2):
    files1 = sorted([f for f in os.listdir(folder1) if f.endswith('.txt')])
    files2 = sorted([f for f in os.listdir(folder2) if f.endswith('.txt')])

    if len(files1) != len(files2):
        return False

    for file1, file2 in zip(files1, files2):
        filepath1 = os.path.join(folder1, file1)
        filepath2 = os.path.join(folder2, file2)

        if read_file(filepath1) != read_file(filepath2):
            return False

    return True

# 使用示例
folder1 = 'D:/jsai/FinalData/jsai_data_copy'
folder2 = 'D:/桌面/jsai_data'
are_folders_same = compare_folders(folder1, folder2)
print(are_folders_same)
