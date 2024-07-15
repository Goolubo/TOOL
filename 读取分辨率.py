from PIL import Image
import os

# 指定要遍历的文件夹路径
folder_path = 'D:/jsai/jsai_data_2'  # 将 '/path/to/your/folder' 替换为实际的文件夹路径

# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否以'.jpg'扩展名结尾
    if filename.endswith('.jpg'):
        file_path = os.path.join(folder_path, filename)  # 获取文件的完整路径
        with Image.open(file_path) as img:
            # 获取图片的分辨率
            image_w, image_h = img.size


