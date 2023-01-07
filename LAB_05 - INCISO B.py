import cv2
import matplotlib.pyplot as plt
import numpy as np

imgg = cv2.imread("Gallito_rocas.jpg",0)

# DESCOMPOSICIÓN EN CAPAS DE BITS DE LA IMAGEN ORIGINAL

imgg_b0 = np.bitwise_and(imgg, 128)
imgg_b1 = np.bitwise_and(imgg, 64)
imgg_b2 = np.bitwise_and(imgg, 32)
imgg_b3 = np.bitwise_and(imgg, 16)
imgg_b4 = np.bitwise_and(imgg, 8)
imgg_b5 = np.bitwise_and(imgg, 4)
imgg_b6 = np.bitwise_and(imgg, 2)
imgg_b7 = np.bitwise_and(imgg, 1)

plt.figure(figsize=(8,5))
plt.subplot(331)
plt.imshow(imgg, cmap="gray")
plt.subplot(332)
plt.imshow(imgg_b0, cmap="gray")
plt.subplot(333)
plt.imshow(imgg_b1, cmap="gray")
plt.subplot(334)
plt.imshow(imgg_b2, cmap="gray")
plt.subplot(335)
plt.imshow(imgg_b3, cmap="gray")
plt.subplot(336)
plt.imshow(imgg_b4, cmap="gray")
plt.subplot(337)
plt.imshow(imgg_b5, cmap="gray")
plt.subplot(338)
plt.imshow(imgg_b6, cmap="gray")
plt.subplot(339)
plt.imshow(imgg_b7, cmap="gray")
plt.show()

# CREAMOS MATRIZ (IMAGEN) DE UNOS CON EL TAMAÑO DE LA  
# IMAGEN ORIGINAL

img=np.ones((imgg.shape), dtype=np.uint8)*255

a0 = np.bitwise_and(img, 128)
a1 = np.bitwise_and(img, 64)
a2 = np.bitwise_and(img, 32)
a3 = np.bitwise_and(img, 16)
a4 = np.bitwise_and(img, 8)
a5 = np.bitwise_and(img, 4)
a6 = np.bitwise_and(img, 2)
a7 = np.bitwise_and(img, 1)

plt.figure(figsize=(8,5))
plt.subplot(331)
plt.imshow(imgg, cmap="gray")
plt.subplot(332)
plt.imshow(a0, cmap="gray")
plt.subplot(333)
plt.imshow(a1, cmap="gray")
plt.subplot(334)
plt.imshow(a2, cmap="gray")
plt.subplot(335)
plt.imshow(a3, cmap="gray")
plt.subplot(336)
plt.imshow(a4, cmap="gray")
plt.subplot(337)
plt.imshow(a5, cmap="gray")
plt.subplot(338)
plt.imshow(a6, cmap="gray")
plt.subplot(339)
plt.imshow(a7, cmap="gray")
plt.show()

# INSERTAMOS UN MENSAJE OCULTO EN LAS ÚLTIMAS 3 CAPAS

cv2.putText(a5, "I", (300,175), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), thickness=8)
cv2.putText(a5, "LIKE", (225,325), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), thickness=8)

cv2.putText(a6, "THE", (250,175), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), thickness=8)
cv2.putText(a6, "NITE", (225,325), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), thickness=8)

cv2.putText(a7, "THE STROKES", (200,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), thickness=8)

plt.figure(figsize=(12,4))
plt.subplot(131)
plt.imshow(a5, cmap="gray")
plt.subplot(132)
plt.imshow(a6, cmap="gray")
plt.subplot(133)
plt.imshow(a7, cmap="gray")
plt.show()

#AGREGAMOS LOS MENSAJES OCULTOS Y CREAMOS LA IMAGEN

plt.figure(figsize=(8,5))
plt.subplot(331)
plt.imshow(imgg, cmap="gray")
plt.subplot(332)
plt.imshow(imgg_b0, cmap="gray")
plt.subplot(333)
plt.imshow(imgg_b1, cmap="gray")
plt.subplot(334)
plt.imshow(imgg_b2, cmap="gray")
plt.subplot(335)
plt.imshow(imgg_b3, cmap="gray")
plt.subplot(336)
plt.imshow(imgg_b4, cmap="gray")
plt.subplot(337)
plt.imshow(imgg_b5, cmap="gray")
plt.subplot(338)
plt.imshow(imgg_b6, cmap="gray")
plt.subplot(339)
plt.imshow(imgg_b7, cmap="gray")
plt.show()

cv2.imwrite("crypted.png",imgg_b0+imgg_b1+imgg_b2+imgg_b3+imgg_b4+a5+a6+a7)

# Comparamos la imagen original con la imagen que tiene 
# mensaje encriptado


plt.figure(figsize=(12,6))
plt.subplot(121)
plt.imshow(imgg, cmap="gray"); plt.title("Imagen original")
plt.subplot(122)
plt.imshow(imgg_b0+imgg_b1+imgg_b2+imgg_b3+imgg_b4+a5+a6+a7, cmap="gray"); plt.title("Encripatada")
plt.show()

# Descomponemos la imagen encriptada en capas de bits 
# para comprobar que existe el mensaje oculto:

image=cv2.imread("crypted.png",0)

f0 = np.bitwise_and(image, 128)
f1 = np.bitwise_and(image, 64)
f2 = np.bitwise_and(image, 32)
f3 = np.bitwise_and(image, 16)
f4 = np.bitwise_and(image, 8)
f5 = np.bitwise_and(image, 4)
f6 = np.bitwise_and(image, 2)
f7 = np.bitwise_and(image, 1)

plt.figure(figsize=(8,5))
plt.subplot(331)
plt.imshow(imgg, cmap="gray")
plt.subplot(332)
plt.imshow(f0, cmap="gray")
plt.subplot(333)
plt.imshow(f1, cmap="gray")
plt.subplot(334)
plt.imshow(f2, cmap="gray")
plt.subplot(335)
plt.imshow(f3, cmap="gray")
plt.subplot(336)
plt.imshow(f4, cmap="gray")
plt.subplot(337)
plt.imshow(f5, cmap="gray")
plt.subplot(338)
plt.imshow(f6, cmap="gray")
plt.subplot(339)
plt.imshow(f7, cmap="gray")
plt.show()