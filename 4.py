import cv2
vid = cv2.VideoCapture(0)
subtractor = cv2.createBackgroundSubtractorMOG2(history=200,varThreshold=500)
while True:
    isOk,frame = vid.read()
    mask_motion = subtractor.apply(frame)
    contours,_ = cv2.findContours(mask_motion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        area = cv2.contourArea(cont)
        if area > 300:
            x,y,w,h = cv2.boundingRect(cont)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow('frame',frame)
    cv2.imshow('mask_moshion',mask_motion)
    k = cv2.waitKey(30)
    if k==27 or isOk==False:
        break
cv2.destroyAllWindows()
vid.release()


