import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def ambil_gambar():
    if not os.path.exists('neg'):
        os.mkdir('neg')

    #Untuk looping ambil gambar. Looping di sesuaikan dengan jumlah gambar
    for num_image in range(50):
        try:
            print('gambar ke-'+str(num_image))
            img = cv2.imread('stop/'+str(num_image+1)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resize_img = cv2.resize(img,(100, 100))
            cv2.imwrite("neg/"+str(num_image+1)+".jpg", resize_img)
        except Exception as e:
            print(str(e))

    print("done!")


def buat_pos_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type=='pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'#jumlah object dalam gambar, asumsinya 1, terus ukurannya 50, 50
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
    print("done!!")

ambil_gambar()
buat_pos_neg()
