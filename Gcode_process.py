import os
input_dir = "E:\\QR_code.txt"
name = os.path.join(input_dir).split(".")[0]
suffix = os.path.join(input_dir).split(".")[1]
onepass = name + "_1pass." + suffix
twopass = name + "_2pass." + suffix


def first_pass():
    oldx = 0
    oldy = 0
    oldline = ""
    with open(input_dir, "r") as f:  # 打开文件,a+可读可写可创建,指针在末尾
        lines = f.readlines()  # 读取文件
        for line in lines:
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            if line:  # 判断字符串为空?
                if line.startswith("END"):
                    break
                else:
                    if line.startswith("G"):
                        if line.find("X") > 0 and line.find("Z") < 0:  # 如果找到了带X的字符,字符下标>0
                            i = line.find("X") + 1
                            j = line.find("Y") - 1
                            x = float(line[i:j])    # 截取X的坐标值并转成浮点数
                            i = line.find("Y") + 1
                            j = line.find("E") - 1
                            y = float(line[i:j])    # 截取y的坐标值并转成浮点数

                            if line.startswith("G1"):
                                with open(onepass, 'a+') as w:
                                    if oldline.startswith("G0"):
                                        # writelines 默认不换行
                                        w.writelines(oldline+'\n')

                                    if ((x-oldx)**2 + (y-oldy)**2)**0.5 > 1:  # 两点之间距离平方根大于1
                                        newline = "G1 X" + \
                                            str(x) + " Y" + str(y)
                                        w.writelines(newline+'\n')
                                        oldx = x
                                        oldy = y
                    oldline = line


def second_pass():
    oldx = 0
    oldy = 0
    with open(onepass, "r") as f:  # 打开文件
        lines = f.readlines()  # 读取文件
        for line in lines:
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            if line:  # 判断字符串为空?
                if line.startswith("END"):
                    break
                else:
                    if line.startswith("G1"):
                        if line.find("X") > 0:  # 如果找到了带X的字符,字符下标>0
                            i = int(line.find("X")) + 1
                            j = int(line.find("Y")) - 1
                            x = float(line[i:j])    # 截取X的坐标值并转成浮点数
                            i = int(line.find("Y")) + 1
                            j = int(line.find("E")) - 1
                            y = float(line[i:j])    # 截取y的坐标值并转成浮点数
                            if ((x-oldx)**2 + (y-oldy)**2)**0.5 > 10:   # 两点之间距离平方根大于10
                                with open(twopass, 'a+') as w:
                                    newline = "G0 X" + str(x) + " Y" + str(y)
                                    w.writelines(newline+'\n')
                            with open(twopass, 'a+') as w:
                                w.write(line+'\n')
                            oldx = x
                            oldy = y
    with open(twopass, 'a+') as w:
        w.write("END"+'\n')


first_pass()
second_pass()
