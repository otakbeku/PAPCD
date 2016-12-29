import numpy as np
import cv2
from matplotlib import pyplot as plot

img_query = cv2.imread('3.jpg',0)
img_train = cv2.imread('template_3.jpg',0)

#TEST DENGAN BRUTE FORCE
sift = cv2.SIFT_create() #ORB =  Oriented FAST and Rotated BRIEF

keypoints1, desc1 = sift.detectAndCompute(img_query,None)
keypoints2, desc2 = sift.detectAndCompute(img_train,None)

#Buat matcher
bf = cv2.BFMatcher()
matches = bf.knnMatch(desc1, desc2, k=2)

#RASIO
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img_result = cv2.drawMatchesknn(img_query,img_train,keypoints2,good,flags=2)

plot.imshow(img_result),plot.show()
