import cv2
import numpy as np

def ajuste_brillo(imagen, alpha, beta):
    return cv2.addWeighted(imagen, alpha, np.zeros(imagen.shape, imagen.dtype), 0, beta)

# Leemos la imagen
imagen = cv2.imread('Gallito_rocas.jpg')

# Aumenta el brillo en un 50%
brillo_imagen = ajuste_brillo (imagen, 1, 50)

# Mosttramos la imagen original y la imagen con el brillo aumentado
cv2.imshow('Original', imagen)
cv2.imshow('Bright', brillo_imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()