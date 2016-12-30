import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


#Instansiasi file cascadenya
stop_cascade = cv2.CascadeClassifier('cascade_stop_sign.xml')

cap = cv2.VideoCapture(0)
tes_uji = 1
#proses segmentasi dan deteksi objek
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    stop = stop_cascade.detectMultiScale(gray, 50, 50)

    #Membuat gambar grayscale
    #abu_abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Untuk ngebuat object kotak saat mendeteksi
    for (x,y,w,h) in stop:
        #untuk Membuat objek kotak
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        #Untuk ngebuat teks atau labelling pada object yang terdeteksi
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'STOP',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
        #Untuk ngecek bisa atau tidak perulangannya
        print("terdeteksi ke-"+str(tes_uji))
        tes_uji+=1

    cv2.imshow('HASIL CASCADE',frame)
    key = cv2.waitKey(1)
    if key == 27: #tombol keluar
        break
    elif key == ord('x'):
        print ("Salaah")

cap.release()
cv2.destroyAllWindows()
