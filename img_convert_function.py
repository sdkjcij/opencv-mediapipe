from cv2 import cv2
import numpy as np

#                # (數值越大膨脹越多)
kernel1 = np.ones((3, 3), np.uint8)

kernel2 = np.ones((3, 3), np.uint8)

img = cv2.imread('C:/Users/user/Desktop/cat2.jpg')
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)

# cvtColor - grayscale 色彩轉換 - 灰階
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# GaussianBlur 高斯模糊
# cv2.GaussianBlur(圖片,(模糊運算範圍), 標準差)
gaussianBlur = cv2.GaussianBlur(img, (15, 15), 0)

# Canny 邊緣檢測
# cv2.Canny(blur_gray, low_threshold, high_threshold)
# -高於 high_threshold 為 strong edge 直接保留
# -介於 low_threshold 與 high_threshold 為 weak edge
# 檢測 weak edge 是否與 strong edge 相連, 如果相連才保留
canny = cv2.Canny(img, 200, 300)

# dilate 膨脹               #陣列     # (膨脹次數)
dilate = cv2.dilate(canny, kernel1, iterations=1)

# erode 侵蝕               #陣列     # (侵蝕次數)
erode = cv2.erode(dilate, kernel1, iterations=1)


cv2.imshow('Img', img)
cv2.imshow('Grayscale', grayscale)
cv2.imshow('GaussianBlur', gaussianBlur)
cv2.imshow('Canny', canny)
cv2.imshow('Dilate', dilate)
cv2.imshow('Erode', erode)
cv2.waitKey(0)
