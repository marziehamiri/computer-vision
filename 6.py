import cv2
import numpy as np

vid = cv2.VideoCapture('Rec 0049.mp4')
subtractor = cv2.createBackgroundSubtractorMOG2(history=10,varThreshold=50)

while True:
    _,frame = vid.read()
    mask = subtractor.apply(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    key = cv2.waitKey(1)
    if key == 27:
        break
vid.release()
cv2.destroyAllWindows()
