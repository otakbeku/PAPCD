import urllib.request
import cv2
import numpy as np
import os

#Untuk ngambil gambar dari url image database
def simpan_raw_image():
    neg_image_link='LINK GAMBAR'
    neg_image_urls=urllib.request.urlopen(neg_image_link).read().decode()
    nomor_gambar = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i,"neg/"+str(nomor_gambar)+".jpg")
            img = cv2.imread("neg/"+str(nomor_gambar)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwirte("neg/"+str(nomor_gambar)+".jpg", resized_image)
            nomor_gambar+=1
        except Exception as e:
            print(str(e))

def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file-type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    if ugly.shape === question.shape and not (np.bitwise_xor(ugly, question).any()):
                        print('gambarnya cacat')
                        os.remove()
                    except Exception as e:
                        print(str(e))
                    


simpan_raw_image()
find_uglies()
