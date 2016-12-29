import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


#this is the cascade we just made. Call what you want
stop_cascade = cv2.CascadeClassifier('cascade_stop_sign.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    stop = stop_cascade.detectMultiScale(gray, 50, 50)

    # add this
    for (x,y,w,h) in stop:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
