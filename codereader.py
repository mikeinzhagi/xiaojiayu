

import cv2
import numpy as np
#im = cv2.imread(r"E:\xiaojiayu\scancode.png")


img = cv2.imread(r"E:\xiaojiayu\scancode.png")
height, width = img.shape[:2]
pattern = []
with open(r"E:\drawing.txt", "a+") as f, open(r"E:\x.txt", "a+") as x, open(r"E:\y.txt", "a+") as y:  # 打开文件
    lines = f.readlines()  # 读取文件
    for i in range(height):
        for j in range(width):
            (b, g, r) = img[i, j]  # 这里可以处理每个像素点
            if b < 10 and g < 10 and r < 10:
                # x.write(str(i)+'\n')
                # y.write(str(j)+'\n')

                #             print(i, j)
                #             pattern.append("*")
                #         else:
                #             pattern.append("-")
                # f.writelines(pattern)
                # pattern = np.array(pattern)
                # print(pattern.reshape(height, width))

                img[i, j] = (255, 0, 0)
#             line = "G1 X" + str(i) + " Y" + str(j)
#             f.write(line+'\n')
# f.write("END"+'\n')

    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
