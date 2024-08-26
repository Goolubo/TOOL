"""
横向裂缝0、纵向裂缝1、块状裂缝2、龟裂3 、坑槽4、修补网状裂缝5、修补裂缝6、修补坑槽7

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

from PIL import Image
import os

# 指定要遍历的文件夹路径
# folder_path = 'D:/jsai/test/image_test'  # 数据集所在的文件夹
folder_path = 'D:/桌面/labels'  # 数据集所在的文件夹
list_data = []          # 用于存储txt文件中每一行的数据
list_content = []       # 以列表存储json文件的标准格式中的点坐标
content_2 = ""    # 用于存储json文件的标准格式

# 遍历文件夹内的所有文件,filename获取文件名（带jpg后缀）
for filename in os.listdir(folder_path):    # 返回指定的文件夹包含的文件或文件夹的名字的列表
    if filename.endswith('.jpg'):           # 测试文件名后缀是否为“.jpg”
        # 处理.txt文件
        txt_filename = os.path.splitext(filename)[0] + '.txt'    # os.path.splitext(filename)[0]：文件名，不包括后缀
        txt_file_path = os.path.join(folder_path, txt_filename)  # 得到txt文件的绝对路径

        # 检查.txt文件是否存在
        if os.path.exists(txt_file_path):
            # 处理.jpg文件
            jpg_file_path = os.path.join(folder_path, filename)
            with Image.open(jpg_file_path) as img:
                # 获取图片分辨率image_w, image_h
                image_w, image_h = img.size
                # 读取.txt文件内容
                with open(txt_file_path, 'r') as txt_file:
                    lines = txt_file.readlines()
                    for line in lines:
                        list_data = line.split(" ")
                        label = int(list_data[0])
                        x_c = float(list_data[1])
                        y_c = float(list_data[2])
                        w = float(list_data[3])
                        h = float(list_data[4])
                        # a, b, c. d是x, y的值
                        a = image_w * x_c - (image_w * w) / 2
                        b = image_w * x_c + (image_w * w) / 2
                        c = image_h * y_c - (image_h * h) / 2
                        d = image_h * y_c + (image_h * h) / 2
                        content_1 = """
    {
      "label": "%d",
      "points": [[%f, %f], [%f, %f], [%f, %f], [%f, %f]],
      "group_id": null,
      "description": "",
      "shape_type": "polygon",
      "flags": {}    
    }
                        """ % (label, a, c, a, d, b, d, b, c)

                        list_content.append(content_1)

                    # 判断什么时候点坐标后面需要加逗号
                    lens = len(list_content)
                    i = 0
                    while i < lens:
                        if i < lens-1:
                            content_2 = content_2 + list_content[i] + ","
                            i += 1
                        else:
                            content_2 = content_2 + list_content[i]
                            i += 1

                    content_3 = """
{
  "version": "5.2.1",
  "flags": {},
  "shapes": [%s],
  "imagePath": "%s",
  "imageData": null,
  "imageHeight": %d,
  "imageWidth": %d
}
                        """ % (content_2, filename, image_h, image_w)

                    # w模式打开文件，将完整的json内容写入json文件
                    f = open(folder_path + "/" + os.path.splitext(filename)[0] + '.json', "w", encoding="UTF-8")
                    f.write(content_3)
                    # 读写完一个文件后，重置content_2和list_content
                    content_2 = ""
                    list_content = []
                    f.close()
