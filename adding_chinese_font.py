from cv2 import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

img1 = cv2.imread('C:/Users/user/Desktop/cat2.jpg')


def cv2ImgAddText(img, text, left, top, textColor, textSize):

    if isinstance(img, numpy.ndarray):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

    draw = ImageDraw.Draw(img)

    fontText = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")

    draw.text((left, top), text, textColor, font=fontText)

    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)


img1 = cv2ImgAddText(img1, "我是貓貓", 100, 50, (0, 255, 0), 60)

cv2.imshow('img1', img1)
cv2.waitKey(0)
