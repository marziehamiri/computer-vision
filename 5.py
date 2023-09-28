import cv2
cap = cv2.VideoCapture(0)
_,Frame = cap.read()
h,w,_ = Frame.shape
vid_format = cv2.VideoWriter_fourcc('M','J','P','G')
output = cv2.VideoWriter('out.mp4',vid_format,25,(w,h))
while True:
    isOk,Frame = cap.read()
    font = cv2.FONT_HERSHEY_COMPLEX 
    gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    _,mask_obj = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(mask_obj,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(Frame,contours,-1,(0,255,0),10)
    for cont in contours:
        approx = cv2.approxPolyDP(cont, 0.009 * cv2.arcLength(cont, True), True) 
         # Used to flatted the array containing 
    # the co-ordinates of the vertices. 
        n = approx.ravel() 
        i = 0

        for j in n : 
            if(i % 2 == 0): 
                x = n[i] 
                y = n[i + 1] 

            # String containing the co-ordinates. 
                string = str(x) + " " + str(y) 

                if(i == 0): 
                # text on topmost co-ordinate. 
                    cv2.putText(Frame, "Arrow tip", (x, y), 
                                font, 0.5, (255, 0, 0)) 
                else: 
                # text on remaining co-ordinates. 
                    cv2.putText(Frame, string, (x, y), 
                        font, 0.5, (0, 255, 0)) 
            i = i + 1
        hull = cv2.convexHull(cont)
        cv2.drawContours(Frame,[hull],-1,(255,0,0),5)
    cv2.imshow('myframe',Frame)
    output.write(Frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
output.release()


