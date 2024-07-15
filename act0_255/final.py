import cv2
import numpy as np
import os


def process_white_areas(img):
    # 将非白色点设为0（黑色），白色点设为255
    _, binary = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)

    # 找到所有的连通区域
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

    # 将每个连通区域内的0值点设为255
    for label in range(1, num_labels):
        mask = labels == label
        if np.any(img[mask] == 0):
            binary[mask] = 255

    return binary

def save_edge_coordinates(image, label_number, file):
    height, width = image.shape[:2]

    # 找边缘
    edges = cv2.Canny(image, 100, 200)
    y_indices, x_indices = np.where(edges == 255)

    # 如果没有白色区域，不写入任何内容
    if len(x_indices) == 0 and len(y_indices) == 0:
        return False

    # 将坐标转换为占图片长宽的比例
    coordinates = ' '.join([f'{x/width:.4f} {y/height:.4f}' for x, y in zip(x_indices, y_indices)])
    file.write(f'{label_number} {coordinates}\n')
    return True

def process_and_save(folder_path, txt_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # 处理白色区域
            processed_img = process_white_areas(img)

            # 创建或打开TXT文件
            base_name = filename.split('-')[0]
            txt_path = os.path.join(txt_folder, f'{base_name}-out_ori.txt')
            with open(txt_path, 'a') as file:
                label_number = filename.split('_')[-1].split('.')[0]
                # 仅在存在白色区域时保存边缘坐标
                if not save_edge_coordinates(processed_img, label_number, file):
                    print(f"文件 {filename} 中没有白色区域。")

# 示例使用
process_and_save('D:/jsai/turn0255/black_images_png', 'D:/jsai/turn0255/black_images_txt')
