# import os
# entries = os.listdir(r'e:\python练习')
# for entry in entries:
#     print(entry)


import os
# 扫描根目录下文件和文件夹名
with os.scandir(r'e:\python练习') as entries:
    for entry in entries:
        print(entry.name)