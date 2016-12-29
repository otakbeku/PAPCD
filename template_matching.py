import cv2
import numpy as np
from matplotlib import pyplot as plt



rgb_gambar = cv2.imread('4.jpg')
abu_abu = cv2.cvtColor(rgb_gambar, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template_4.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(abu_abu,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(rgb_gambar, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('resasdyoaisd.jpg',rgb_gambar)


img = cv2.imread('resulst.jpg', cv2.IMREAD_GRAYSCALE)
resize_img = cv2.resize(img,(100,100))
cv2.imshow(rgb_gambar)
cv2.waitkey(0)
cv2.destroyAllWindows()
