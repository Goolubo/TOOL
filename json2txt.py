"""

目标类别，x_center, y_center, w, h，
其中 x_center, y_center 表示目标中心点坐标占图片长和高的比例; w, h 表示目标长和高占图片的比例。
- H * W = 1080 * 1920
- 1 0.475521 0.733333 0.036458 0.087037
- 目标类别：1
- x_center = 0.475521
- y_center = 0.733333
- w = 0.036458
- h = 0.087037
"""

import os
import json
from PIL import Image

# 指定要读取的文件夹路径
folder_path = 'D:/图片/bricycle2-6.19'     # 将***替换为包含json文件的文件目录

# 获取文件夹中的所有.json文件
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# 遍历每个JSON文件并提取数据
for json_file in json_files:
    file_path = os.path.join(folder_path, json_file)

    # 获得每个图片的分辨率
    jpg_file_path = file_path.replace('.json', '.jpg')
    with Image.open(jpg_file_path) as img:
        # 获取图片分辨率image_w, image_h
        image_w, image_h = img.size

    # 打开JSON文件并解析数据
    with open(file_path, 'r') as f:
        data = json.load(f)

    # 数据定义
    lens = len(data['shapes'])
    list_content = []
    txt_name = json_file.replace('.json', '.txt')

    # 循环访问json文件的矩形框数据
    for lab in data['shapes']:
        # 读取标签
        label = lab['label']

        # 计算x_center, y_center, w, h
        list_x = []
        list_y = []
        point_list = lab['points']
        for i in point_list:
            list_x.append(i[0])
            list_y.append(i[1])
        x_max = max(list_x)
        x_min = min(list_x)
        y_max = max(list_y)
        y_min = min(list_y)
        x_center = ((x_max - x_min)/2 + x_min) / image_w
        y_center = ((y_max - y_min)/2 + y_min) / image_h
        w = (x_max - x_min) / image_w
        h = (y_max - y_min) / image_h

        # 将每一行数据添加进一个列表中，每行结束后回车
        list_content.append(str(label) + " " + str(x_center) + " " + str(y_center) + " " + str(w) + " " + str(h))
        list_content.append("\n")

    # 将数据写入txt文件，覆盖原先的txt文件
    f = open(folder_path + "/" + txt_name, "w", encoding="utf-8")
    for i in list_content:
        i = str(i)
        f.write(i)
    f.close()


