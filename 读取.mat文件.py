import scipy.io
import pandas as pd

# 指定 .mat 文件的路径
file_path = "D:/桌面/2024年江苏省研究生数学建模科研创新实践大赛C题/LeftRadar.mat"

# 使用 scipy.io.loadmat 函数读取 .mat 文件
mat_data = scipy.io.loadmat(file_path)

# 创建一个 Pandas 的 ExcelWriter 对象
excel_file = 'output1.xlsx'
writer = pd.ExcelWriter(excel_file, engine='openpyxl')

# 遍历 mat_data 中的所有键，将每个键的数据写入 Excel 文件
for key, value in mat_data.items():
    # 跳过 MATLAB 文件的 meta 数据
    if key.startswith('__'):
        continue

    # 将数据转换为 DataFrame
    df = pd.DataFrame(value)

    # 将 DataFrame 写入 Excel 文件
    df.to_excel(writer, sheet_name=key, index=False)

# 保存 Excel 文件
writer.save()

print(f'所有数据已成功保存到 {excel_file}')
