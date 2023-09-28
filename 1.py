import cv2
cap = cv2.VideoCapture(0)
while True:
    isOk,Frame = cap.read()
    cv2.imshow('myframe',Frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()


