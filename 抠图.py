from removebg import RemoveBg
import win32ui
import os
dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
dlg.SetOFNInitialDir(r'D:\OpenCV')  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName()  # 获取选择的文件名称
path = os.path.dirname(filename)  # 获取该文件上一级文件夹(目的是选择该文件夹内所有图片)
rmbg = RemoveBg("fUz4tqqcTruPpm6y5j2y4MNz", "error.log")  # 引号内是你获取的API
for pic in os.listdir(path):
    rmbg.remove_background_from_img_file(os.path.join(path, pic))
    # print (os.path.join(path, pic))
    # print (filename)
# rmbg.remove_background_from_img_file(filename)  # 图片地址
