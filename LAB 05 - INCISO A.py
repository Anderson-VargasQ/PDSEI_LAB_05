import cv2
import matplotlib.pyplot as plt
import numpy as np
vect = np.zeros((256))
imgg = cv2.imread("Gallito_rocas.jpg", 0)
s = np.zeros(imgg.shape)

for i in range(imgg.shape[0]):
    for j in range(imgg.shape[1]):
        s[i,j] = vect[imgg[i,j]]
        
plt.imshow(s, cmap="gray")       
plt.show()

vect = np.zeros((256))

for i in range(256):
    if i < 75:
        vect[i] = i
    if 75 <=i and i< 125:
        vect[i] = 225
    if 125 <=i:
        vect[i] = i + 10

img = cv2.imread('Gallito_rocas.jpg',0)
s=cv2.LUT(img, vect)
plt.figure(figsize=(8,5))
plt.imshow(s, cmap='gray')
plt.show()

