import numpy as np
import cv2

# 1.加载图片，转为二值图
img = cv2.imread(r'D:\OpenCV\1\10.png')
drawing = np.zeros(img.shape[:], dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)


# 3.统计概率霍夫线变换
lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 90, minLineLength=550, maxLineGap=8)

# 3.将检测的线画出来
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)


cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
