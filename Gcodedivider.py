import linecache
import os

counter = 0
lineNum = 0
linelist = []
with open(r"F:\ABB_Gcode.txt", "r") as f:
    lines = f.readlines()  # 读取文件
    # for line in lines:
    #     if line.startswith(";LAYER"):
    #         counter += 1
    # print("该模型分为", counter, "层", sep="")
    for line in lines:
        lineNum = lineNum + 1
        if ";LAYER" in line.strip():
            counter += 1
            linelist.append(lineNum)  # 将行号加入行列表
            print("第", counter, "个LAYER在第", lineNum, "行", sep="")
    print("该模型一共", counter, "层", sep="")
    print(linelist)
    for i in range(counter - 1):
        newline = linecache.getlines(r"D:\BaiduNetdiskDownload\Gcode_drawing\test.txt")[
            linelist[i]-1: linelist[i + 1]-1
        ]
        with open(
            os.path.join("D:\BaiduNetdiskDownload\Gcode_drawing",
                         "Layer" + str(i) + ".txt"), "a+"    # 根据i的名称建立文件
        ) as w:
            w.writelines(newline)
