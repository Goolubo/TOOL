from PIL import Image

def is_binary_image(image_path):
    with Image.open(image_path) as img:
        # 获取所有独特的像素值
        unique_pixels = set(img.getdata())

        # 检查是否只包含0和255
        return unique_pixels == {0, 255}

# 示例用法
image_path = 'D:/jsai/1/24.png'  # 替换为您的图片路径
is_binary = is_binary_image(image_path)  # 使用之前保存的PNG格式二值图
print(f"该图像是{'二值图' if is_binary else '非二值图'}")
