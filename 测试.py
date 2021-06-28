
import numpy as np
import cv2
import math
import win32ui
import os
dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
dlg.SetOFNInitialDir(r'D:\OpenCV')  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName()  # 获取选择的文件名称
#image = cv2.imread(filename)
path = os.path.dirname(filename)  # 获取该文件上一级文件夹(目的是选择该文件夹内所有图片)
def Auto():
    print("img")

for img in os.listdir(path):
    img = os.path.join(path, img)
    print(img)
    Auto()



