import os

folder_path = "D:/jsai/FinalData2/old/di_done"

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    # 使用1时先把2注释掉，使用2时把1注释掉

    # step1:先删除所有矩形框的txt文件
    # if "jpg.txt.txt" not in filename and filename.endswith(".txt"):
    #     file_path = os.path.join(folder_path, filename)
    #     os.remove(file_path)
    #     print(f"Deleted file: {filename}")

    # # step2：规范txt文件名
    if ".jpg.txt" in filename:
        new_filename = filename.replace(".jpg.txt", "")  # 删除文件名中的".jpg.txt"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        # 重命名文件
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

