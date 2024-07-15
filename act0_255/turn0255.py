from PIL import Image
import os
import glob

def convert_images_to_binary_png(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 在输入文件夹中找到所有的jpg图像
    jpg_images = glob.glob(os.path.join(input_folder, "*.jpg"))

    # 处理每张图像
    i = 0
    for image_path in jpg_images:
        # 打开图像
        with Image.open(image_path) as img:
            # 首先转换为灰度图
            grayscale_img = img.convert("L")
            # 将灰度图转换为二值图（只包含0和255）
            binary_img = grayscale_img.point(lambda x: 0 if x < 128 else 255, '1')
            # 在PNG格式下保存二值图到输出文件夹
            file_name = os.path.splitext(os.path.basename(image_path))[0] + ".png"
            binary_img.save(os.path.join(output_folder, file_name), format='PNG')
        i += 1
        print(i)
    return len(jpg_images)

# 示例输入和输出文件夹路径
input_folder = "D:/jsai/turn0255/black_images"  # 替换为您的输入文件夹路径
output_folder = "D:/jsai/turn0255/black_images_png"      # 替换为您的输出文件夹路径

# 转换并保存图像
num_converted = convert_images_to_binary_png(input_folder, output_folder)
print(f"已转换 {num_converted} 张图像")
