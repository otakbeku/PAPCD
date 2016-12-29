import cv2
import numpy as np
from matplotlib import pyplot as plt

query = cv2.imread('3.jpg',0)
query_copy = query.copy()
template = cv2.imread('template_3.jpg',0)
w, h = template.shape[::-1]


methods=['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for methodke in methods:
    query = query_copy.copy()
    method = eval(methodke)

    res = cv2.matchTemplate(query,template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        atas_kiri = min_loc
    else:
        atas_kiri = max_loc
    bawah_kanan = (atas_kiri[0]+w, atas_kiri[1]+h)

    cv2.rectangle(query, atas_kiri, bawah_kanan, 255,2)

    plt.subplot(121), plt.imshow(res, cmap ='gray')
    plt.title('coba tm result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(query,cmap='gray')
    plt.title('Terdeteksi'),plt.xticks([]),plt.yticks([])
    plt.suptitle(methodke)

    plt.show()
