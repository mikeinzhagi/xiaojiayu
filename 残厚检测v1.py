
import numpy as np
import cv2
import math
import win32ui
import os


def Automeasure(img):
    # step1：加载图片，转成灰度图
    image = cv2.imread(img)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    width, height = image.shape[:2]
    # step2:用Sobel算子计算x，y方向上的梯度，之后在x方向上减去y方向上的梯度，通过这个减法，我们留下具有高水平梯度和低垂直梯度的图像区域。

    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    # step3：去除图像上的噪声。首先使用低通滤泼器平滑图像（9 x 9内核）,这将有助于平滑图像中的高频噪声。
    # 低通滤波器的目标是降低图像的变化率。如将每个像素替换为该像素周围像素的均值。这样就可以平滑并替代那些强度变化明显的区域。
    # 然后，对模糊图像二值化。梯度图像中不大于90的任何像素都设置为0（黑色）。 否则，像素设置为255（白色）。

    # blur and threshold the image
    blurred = cv2.blur(gradient, (9, 9))
    ret, thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # perform a series of erosions and dilations
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    # 开运算
    ret, th2 = cv2.threshold(closed, 0.1, 255, cv2.THRESH_BINARY)
    kernel = np.ones((10, 10), np.uint8)
    opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel, iterations=2)

    # 腐蚀
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(opening, kernel, iterations=2)
    # cv2.imshow("contours", opening)
    # cv2.waitKey(0)

    # 找出边界
    contours, hierarchy = cv2.findContours(
        erosion.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 获取最大轮廓
    c = sorted(contours, key=cv2.contourArea, reverse=True)[0]

    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    shape = np.trunc(rect[0])
    shaped = shape.astype(int)

    # # draw a bounding box arounded the detected barcode and display the image
    # cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
    # cv2.imshow("Image", image)
    # cv2.imwrite("contoursImage2.jpg", image)
    # cv2.waitKey(0)

    # 1.加载图片，转为二值图
    drawing = np.zeros(shaped, dtype=np.uint8)

    edges = cv2.Canny(gray, 50, 150)

    # 3.统计概率霍夫线变换
    lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 90,
                            minLineLength=height*0.95, maxLineGap=10)

    if lines.any:
        # 3.将检测的线画出来
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 1)

        cv2.namedWindow("Image")
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
dlg.SetOFNInitialDir(r'D:\OpenCV')  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName()  # 获取选择的文件名称
#image = cv2.imread(filename)
path = os.path.dirname(filename)  # 获取该文件上一级文件夹(目的是选择该文件夹内所有图片)
for img in os.listdir(path):
    img = os.path.join(path, img)
    Automeasure(img)


# cv2.namedWindow("Image")
# cv2.imshow("Image", closed)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
