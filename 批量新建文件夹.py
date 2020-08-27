import os
meilong = ['爸爸', '妈妈', '老婆', '皮蛋', '大王']
for i in range(len(meilong)):
    print(meilong[i])
    os.chdir(r'e:\python练习')   # 指定文件夹目录(目录不存在程序就无法运行)
    os.makedirs(meilong[i])    # 根据列表内容建立文件夹
