import cv2
import numpy as np
from matplotlib import pyplot as plt

i =0
img = cv2.imread('stop/'+str(i+1)+'.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
