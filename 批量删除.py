import os

def delete_json_files(directory):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以 .json 结尾
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            # 删除文件
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# 示例用法
target_folder = 'D:/图片/bic/bicycle2'  # 替换为实际的目标文件夹路径

delete_json_files(target_folder)
