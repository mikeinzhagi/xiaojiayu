import numpy as np
import cv2

img = cv2.imread(r'D:\OpenCV\1\1.png')

img = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯模糊  去噪 以免影响边缘检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 250, apertureSize=3)  # 边缘检测

cv2.namedWindow("Image")
cv2.imshow("Image", gray)
#cv2.imshow("Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("canny.jpg", edges) 
