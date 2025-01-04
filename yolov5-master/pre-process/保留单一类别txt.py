# import os
#
# # 设置各数据集的标签文件夹路径
# datasets = {
#     'train': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/train/labels',
#     'valid': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/valid/labels',
#     'test': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/test/labels'
# }
#
# # 设置新的目标文件夹路径，用于存储筛选后的标签文件
# output_folders = {
#     'train': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/train/labels_bus_only',
#     'valid': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/valid/labels_bus_only',
#     'test': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/test/labels_bus_only'
# }
#
# # 创建目标文件夹（如果不存在的话）
# for folder in output_folders.values():
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#
# # bus 类别的索引，假设 bus 在 data.yaml 文件中的索引为 2
# bus_class_index = 2
#
# # 遍历所有数据集的标签文件夹
# for dataset, labels_path in datasets.items():
#     print(f"正在处理 {dataset} 数据集的标签文件...")
#
#     # 获取当前数据集对应的输出文件夹路径
#     output_folder = output_folders[dataset]
#
#     # 遍历标签文件夹中的所有标签文件
#     for label_file in os.listdir(labels_path):
#         # 只处理以 .txt 结尾的文件
#         if label_file.endswith('.txt'):
#             label_path = os.path.join(labels_path, label_file)
#
#             # 打开标签文件读取内容
#             with open(label_path, 'r') as f:
#                 lines = f.readlines()
#
#             # 过滤掉不是 bus 类别的标注，保留 bus 类别的标注
#             bus_lines = [line for line in lines if int(line.split()[0]) == bus_class_index]
#
#             # 如果有 bus 类别的标注，创建新文件保存
#             if bus_lines:
#                 # 创建新文件名，后缀添加 '_bus_only'
#                 new_label_path = os.path.join(output_folder, label_file.replace('.txt', '_bus_only.txt'))
#
#                 # 将筛选后的标注写入新文件
#                 with open(new_label_path, 'w') as f:
#                     f.writelines(bus_lines)
#             else:
#                 # 如果没有 bus 类别的标注，可以选择删除空文件，或者不做任何操作
#                 # 这里我们选择不处理，或者可以创建一个空文件作为标识
#                 pass
#
# print("处理完成，所有标签文件中已只保留 bus 类别的标注，并保存在新的文件夹中。")

##################### 保留空标签
import os

# 设置各数据集的标签文件夹路径
datasets = {
    'train': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/train/labels',
    'valid': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/valid/labels',
    'test': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/test/labels'
}

# 设置新的目标文件夹路径，用于存储筛选后的标签文件
output_folders = {
    'train': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/train1/labels_bus_only',
    'valid': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/valid1/labels_bus_only',
    'test': 'D:/BaiduNetdiskDownload/Final.v1i.yolov5pytorch/test1/labels_bus_only'
}

# 创建目标文件夹（如果不存在的话）
for folder in output_folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# bus 类别的索引，假设 bus 在 data.yaml 文件中的索引为 2
bus_class_index = 2

# 遍历所有数据集的标签文件夹
for dataset, labels_path in datasets.items():
    print(f"正在处理 {dataset} 数据集的标签文件...")

    # 获取当前数据集对应的输出文件夹路径
    output_folder = output_folders[dataset]

    # 遍历标签文件夹中的所有标签文件
    for label_file in os.listdir(labels_path):
        # 只处理以 .txt 结尾的文件
        if label_file.endswith('.txt'):
            label_path = os.path.join(labels_path, label_file)

            # 打开标签文件读取内容
            with open(label_path, 'r') as f:
                lines = f.readlines()

            # 过滤掉不是 bus 类别的标注，保留 bus 类别的标注
            bus_lines = [line for line in lines if int(line.split()[0]) == bus_class_index]

            # 如果有 bus 类别的标注，创建新文件保存
            if bus_lines:
                # 创建新文件名，后缀添加 '_bus_only'
                new_label_path = os.path.join(output_folder, label_file.replace('.txt', '_bus_only.txt'))

                # 将筛选后的标注写入新文件
                with open(new_label_path, 'w') as f:
                    f.writelines(bus_lines)
            else:
                # 对于没有 bus 类别的图片，创建一个空的标签文件
                new_label_path = os.path.join(output_folder, label_file.replace('.txt', '_bus_only.txt'))
                with open(new_label_path, 'w') as f:
                    pass  # 创建一个空的标签文件

print("处理完成，所有标签文件中已只保留 bus 类别的标注，并保存在新的文件夹中。")
