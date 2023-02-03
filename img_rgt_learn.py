from cv2 import cv2
# 注意檔名必須為英文
img_path = 'C:/Users/user/Desktop/img1.jpg'
window_name = 'image'
img = cv2.imread(img_path)
# 改變圖片大小
img = cv2.resize(img, (300, 300))
# 以倍數改變圖片大小
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow(window_name, img)
cv2.waitKey(2)

video_path = 'C:/Users/user/Desktop/video1.mp4'

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break
