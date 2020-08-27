import os
data_file = r'e:\python练习\列表.py'
# 如果类型是文件则进行删除
if os.path.is_file(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')

############################################################### 无法执行