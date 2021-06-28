oldx = 0
oldy = 0
with open(r"D:\BaiduNetdiskDownload\Gcode_drawing\faurecia_1pass.txt", "r") as f:  # 打开文件
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
                            with open(r"D:\BaiduNetdiskDownload\Gcode_drawing\faurecia_2pass.txt", 'a+') as w:
                                newline = "G0 X" + str(x) + " Y" + str(y)
                                w.writelines(newline+'\n')
                        with open(r"D:\BaiduNetdiskDownload\Gcode_drawing\faurecia_2pass.txt", 'a+') as w:
                            w.write(line+'\n')
                        oldx = x
                        oldy = y
