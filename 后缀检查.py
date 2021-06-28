# import os
# # 只返回根目录下的该后缀文件,下层文件不返回
# for f_name in os.listdir(r'e:\python练习'):
#     if f_name.endswith('.py'):
#         print(f_name)

# import os
# import fnmatch
# # 使用 fnmatch 进行简单文件名模式匹配
# for f_name in os.listdir(r'e:\python练习'):
#     if fnmatch.fnmatch(f_name, '*.py'):
#         print(f_name)

# # 在当前目录下查询所有Python代码文件
# import glob
# import os
# os.chdir(r'e:\python练习')  # 改变工作目录到e:\python练习
# print(glob.glob('*.py'))


# glob在子目录中递归的搜索文件

import glob
import os
os.chdir(r'e:\python练习')  # 改变工作目录到e:\python练习
for name in glob.iglob('**/*.py', recursive=True):
    print(name)
