import cv2
import matplotlib.pyplot as plt
import numpy as np

# Lectura de imágenes

img1 = cv2.imread("image_48.jpg", 0)
img2 = cv2.imread("image_5.jpg", 0)

# Realizamos las ecualizaciones de las imagenes
equ_img1 = cv2.equalizeHist(img1)
equ_img2 = cv2.equalizeHist(img2)

# Ecualización de la primera imagen

Fx = list(range(256))
Fy = np.zeros(256)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        Fy[img1[i, j]] = equ_img1[i, j]

# Ecualización de la segunda imagen

Fy1 = np.zeros(256)

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        Fy1[img2[i, j]] = equ_img2[i, j]

# Función de comparaciónde colores Imagen 1 y la Imagen 2

Fy2 = np.zeros(256)

for i in range(Fy.shape[0]):
    Fy2[i] = i

for i in range(Fy.shape[0]):
    for j in range(Fy1.shape[0]):
        if Fy1[j] == Fy[i]:
            Fy2[i] = j

# Aplicamos la transformacion Fy2

img_T = cv2.LUT(img1, Fy2)

# Imprimimos las 3 imágenes e histogramas

plt.figure(figsize=(8,5))

plt.subplot(321)
plt.imshow(img1, cmap="gray")
plt.title("Objetivo")
plt.subplot(322)
plt.hist(img1.ravel(), 256, [0, 256])
plt.title(" Histograma de la Imagen 1")

plt.subplot(323)
plt.imshow(img2, cmap="gray")
plt.title("Referencia")
plt.subplot(324)
plt.hist(img2.ravel(), 256, [0, 256])
plt.title(" Histograma de la Imagen 2")

plt.subplot(325)
plt.imshow(img_T, cmap="gray")
plt.title("Resultado")
plt.subplot(326)
plt.hist(img_T.ravel(), 256, [0, 256])
plt.title(" Histograma de la Imagen 1 Transformada")

plt.show()