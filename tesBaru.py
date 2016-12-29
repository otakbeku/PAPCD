import cv2
import numpy as np
from matplotlib import pyplot as plot


def template_matching(rgb_gambar, index_frame):
    abu_abu = cv2.cvtColor(rgb_gambar, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('template_4.jpg',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(abu_abu,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(rgb_gambar, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imwrite('result'+str(index_frame)+".jpg",rgb_gambar)
        print('Terdeteksi')
    return rgb_gambar

#segmentasi
cam = cv2.VideoCapture(0)
template = cv2.imread('template_4.jpg',0)
w, h = template.shape[::-1]
index_frame =0
while(True):
    tf, frame = cam.read()
    #print (' gambarnya bisa/takenya bisa')
    index_frame += 1
    frame2 = template_matching(frame, index_frame)

    #dekomposisi
    abu_abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(abu_abu,template,cv2.TM_CCOEFF_NORMED)

    cv2.imshow('gambar per frame', frame2)
    cv2.imshow('frame abu-abu', abu_abu)

    #cv2.imshow('Single frame', frame)
    key = cv2.waitKey(1)
    if key == 27: #tombol keluar
        break
    elif key == ord('x'):
        print ("Salaah")

cv2.imshow('template',template)

cam.release()
cv2.destroyAllWindows()
