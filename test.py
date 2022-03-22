import cv2

face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
img = cv2.imread(
    "C:/Users/mines/OneDrive/Desktop/Crowd-of-Diverse-People_800x528-768x512.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()
