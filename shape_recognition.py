from cv2 import cv2

shape = cv2.imread('C:/Users/user/Desktop/img3).jpg')
img_contour = shape.copy()
shape = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(shape, 100, 150)
contour, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contour:
    area = cv2.contourArea(cnt)
    # print(cv2.contourArea(cnt))
    cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
    if area > 500:
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
        print(len(vertices))

# cv2.imshow('shape', shape)
cv2.imshow('canny', canny)
cv2.imshow('img_contour', img_contour)
cv2.waitKey(0)
