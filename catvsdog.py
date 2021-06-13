import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR="C:/Users/Galaxy/Documents/Anaconda(Spyder)/catvsdog/PetImages"
CATAGORIES=["Cat","Dog"]

for category in CATAGORIES:
    path=os.path.join(DATADIR, category)# path to cats and dogs
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array,cmap="gray")
        plt.show()
        break
    break
print(img_array)
print(img_array.shape)

IMG_SIZE=30

new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
plt.imshow(new_array,cmap="gray")
plt.show()
