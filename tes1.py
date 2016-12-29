import numpy as np
import cv2


img = cv2.imread('3.jpg', cv2.IMREAD_GRAYSCALE)
resize_img = cv2.resize(img,(100,100))
cv2.imshow('gambar', resize_img)
cv2.waitkey(0)
cv2.destroyAllWindows()
