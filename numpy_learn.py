from cv2 import cv2
import numpy as np
import random
# img = cv2.imread('C:/Users/user/Desktop/img1.jpg')
# print(img)
# print(type(img))
# print(img.shape)

# img.shape(x,y,z) =>
# [
#    [[3個值],[3個值],[3個值]...y個],
#    [[3個值],[3個值],[3個值]...y個],
#    [[3個值],[3個值],[3個值]...y個],
#    ...x個
# ]

# [B,G,R]

img_numpy = np.empty([255, 255, 3], np.uint8)

for B_color in range(255):
    for G_color in range(255):
        for R_color in range(255):
            img_numpy[B_color][G_color] = [B_color, G_color, R_color]


img_chaos = np.empty([255, 255, 3], np.uint8)

for row in range(255):
    for col in range(255):
        img_chaos[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

half_img_numpy = img_numpy[:127, :127]
cv2.imshow('img_numpy', img_numpy)
cv2.imshow('img_chaos', img_chaos)
cv2.imshow('half_img_numpy', half_img_numpy)
cv2.waitKey(0)
