import cv2
import os
import numpy as np


def process_image(image_path, output_txt_path):
    # 读取灰度图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"无法读取图像: {image_path}")

    height, width = image.shape
    labels = []

    # 检测每个灰度值（1, 2, 3）的边界
    for class_id in [1, 2, 3]:
        # 创建一个二值图像
        binary_image = np.where(image == class_id, 255, 0).astype(np.uint8)

        # 查找边界
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # 获取多边形边界
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # 获取边界坐标并归一化
            coords = approx.flatten().tolist()
            coords = [coords[i] / width if i % 2 == 0 else coords[i] / height for i in range(len(coords))]

            # 检查归一化后的坐标
            for coord in coords:
                if coord < 0 or coord > 1:
                    print(f"错误: 归一化后的坐标 {coord} 超出范围。文件: {image_path}")

            coords_str = ' '.join(map(str, coords))
            labels.append(f"{class_id} {coords_str}")

    # 将标签写入txt文件
    with open(output_txt_path, 'w') as f:
        for label in labels:
            f.write(label + '\n')


def process_dataset(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(input_folder, filename)
            output_txt_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
            process_image(image_path, output_txt_path)
            print(f"处理完成: {filename}")


# 示例使用
input_folder = 'D:/code/github/yolo-v8/ultralytics-main/NEU_Seg-main/annotations/test'  # 输入图像文件夹路径
output_folder = 'D:/code/github/yolo-v8/ultralytics-main/NEU_Seg-main/labels/text'  # 输出txt标签文件夹路径

process_dataset(input_folder, output_folder)
