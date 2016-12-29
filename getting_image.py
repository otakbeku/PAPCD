import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def ambil_gambar():
    if not os.path.exists('neg'):
        os.mkdir('neg')

    #Untuk looping ambil gambar. Looping di sesuaikan dengan jumlah gambar
    for num_image in range(50):
        print('gambar ke-'+str(i))
        img = cv2.imread('stop/'+str(i+1)+'.jpg',cv2.IMREAD_GRAYSCALE)
        resize_img = cv2.resize(img,(100, 100))
        cv2.imwrite("neg/"+str(i+1)+".jpg", resize_img)
