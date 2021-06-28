import os
os.chdir(r'E:\Python PDF')  # 改变工作目录到e:\python练习
for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)

# os.walk()
# 在每个循环中返回三个值：
#
# 当前文件夹的名称
# 当前文件夹中子文件夹的列表
# 当前文件夹中文件的列表