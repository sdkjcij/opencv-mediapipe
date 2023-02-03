from cv2 import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)

#            # 初位置  # 末位置    # 顏色  # 粗度
cv2.line(img, (0, 0), (400, 400), (255, 0, 0), 1)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 1)

#                # 初位置   # 末位置      # 顏色  # 粗度
cv2.rectangle(img, (0, 0), (400, 300), (0, 255, 180), 2)
# cv2.rectangle(img, (0,0), (400,300), (0,255,180), cv2.FILLED)
cv2.rectangle(img, (100, 100), (300, 200), (150, 30, 180), cv2.FILLED)

#               # 中心位置 #半徑    # 顏色        # 粗度
cv2.circle(img, (300, 300), 50, (140, 190, 240), cv2.FILLED)

#                       # 左下角位置      # 字體     # 大小    #顏色
cv2.putText(img, 'Dick', (400, 400), cv2.FONT_ITALIC, 2, (255.255, 255))

cv2.imshow('img', img)
cv2.waitKey(0)
