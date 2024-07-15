import os
import shutil
# 指定要操作的文件夹路径
folder_path = "D:/jsai/test/txt_file_test"

# 遍历文件夹中的所有文件
# for filename in os.listdir(folder_path):
#     # 检查是否是文件而不是文件夹
#     if os.path.isfile(os.path.join(folder_path, filename)):
#         # 分离文件名和扩展名
#         name, extension = os.path.splitext(filename)
#         # 在前缀名后面添加"_0"，然后重新构建文件名
#         new_filename = name + "_0" + extension
#         # 构建新的文件路径
#         new_filepath = os.path.join(folder_path, new_filename)
#         # 重命名文件
#         os.rename(os.path.join(folder_path, filename), new_filepath)
# print("文件前缀名后面已添加'_0'")

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查是否是文件而不是文件夹
    if os.path.isfile(os.path.join(folder_path, filename)):
        # 分离文件名和扩展名
        name, extension = os.path.splitext(filename)

        # 复制文件100次
        for i in range(100):
            new_filename = f"{name}_{i}{extension}"
            source_filepath = os.path.join(folder_path, filename)
            destination_filepath = os.path.join(folder_path, new_filename)
            shutil.copy2(source_filepath, destination_filepath)

        # 删除源文件
        source_filepath = os.path.join(folder_path, filename)
        os.remove(source_filepath)

print("文件已复制并删除源文件")

