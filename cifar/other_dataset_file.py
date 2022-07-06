import numpy as np
import pickle
from PIL import Image
import sys,os
import skimage.io
from skimage.io import imread_collection

data = []
labels = []
dir_path= ['datasets/Produce3Classes/fuji_apple/*.jpg',
            'datasets/Produce3Classes/honneydew_melon/*.jpg',
            'datasets/Produce3Classes/taiti_lime/*.jpg']


"""
img = Image.open('datasets/Produce3Classes/fuji_apple/fuji_apple_001.jpg')
img_ndarray = np.asarray(img, dtype='float64')/255


red= np.ndarray.flatten(img_ndarray[:,:,0], order='C')
green= np.ndarray.flatten(img_ndarray[:,:,1], order='C')
blue = np.ndarray.flatten(img_ndarray[:,:,2], order='C')
flat_img = np.concatenate([red,green,blue])

print(np.shape(flat_img))
print(flat_img[:10])
"""

dir_path = 'datasets/dataset_eucapytus/dataset-1/*.png'
images_path = 'datasets/dataset_eucapytus/dataset-1'

files = os.listdir(images_path)
files = np.sort(files)
labels = []
for txt in files:
   n = int(txt.split('.')[0][-1]) #obtem a classe da imagem pelo ultimo caracter do nome do arquivo
   labels.append(int(n+1))


#labels = np.array(labels)
col_img = imread_collection(dir_path)
col_img = col_img.concatenate()
for img in range(len(col_img)):
    img_ndarray = np.asarray(col_img[img], dtype='uint8')
    red= np.ndarray.flatten(img_ndarray[:,:,0], order='C')
    green= np.ndarray.flatten(img_ndarray[:,:,1], order='C')
    blue = np.ndarray.flatten(img_ndarray[:,:,2], order='C')
    flat_img = np.concatenate([red,green,blue])

    data.append(flat_img.copy())

'''
i=2
col_img = imread_collection(dir_path[i])
col_img = col_img.concatenate()
print(len(col_img))
for img in range(len(col_img)):
    img_ndarray = np.asarray(col_img[img], dtype='uint8')
    red= np.ndarray.flatten(img_ndarray[:,:,0], order='C')
    green= np.ndarray.flatten(img_ndarray[:,:,1], order='C')
    blue = np.ndarray.flatten(img_ndarray[:,:,2], order='C')
    flat_img = np.concatenate([red,green,blue])

    data.append(flat_img.copy())
    labels.append(i)

print(labels)
'''
print(labels)
dict = {b'data': data,
        b'labels': labels
        }
with open('data'+str(1), 'wb') as fh:
    pickle.dump(dict, fh)





