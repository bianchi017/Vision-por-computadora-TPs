#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Realizado en Python 2.7 con opencv-python 3.4.2.16 y opencv-contrib-python 3.4.2.16
import numpy as np
import cv2

MIN_MATCH_COUNT = 10
img1 = cv2.imread('notebook1.jpg')
img2 = cv2.imread('notebook2.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Inicializamos el detector y el descriptor
dscr = cv2.xfeatures2d.SIFT_create()

# Encontramos los puntos clave y los descriptores con SIFT en las dos imágenes
kp1, des1 = dscr.detectAndCompute(gray1, None)
kp2, des2 = dscr.detectAndCompute(gray2, None)

# Encontrar las correspondencias
matcher = cv2.BFMatcher(cv2.NORM_L2)
# Guardar las correspondencias
matches = matcher.knnMatch(des1, des2, k=2)

# Guardamos los buenos matches usando el test de razón de Lowe
good = []
for m, n in matches:
    if m.distance < 0.70 * n.distance:
        good.append(m)

if len(good) > MIN_MATCH_COUNT:
    print'Las coincidencias encontradas:', len(good), ', superan el mínimo establecido de', MIN_MATCH_COUNT
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    # Computamos la homografía con RANSAC
    H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)
else:
    print'Las coincidencias encontradas:', len(good), ', no superan el mínimo establecido de', MIN_MATCH_COUNT
    exit()

# Aplicamos la trasformación perspectiva H a la imagen 2
wimg2 = cv2.warpPerspective(img2, H, img1.shape[1::-1])

# Mezclamos ambas imágenes
alpha = 0.5
blend = np.array(wimg2 * alpha + img1 * (1 - alpha), dtype=np.uint8)

# Guardamos y mostramos el resultado
cv2.imwrite('MezclaImg.jpg', blend)
cv2.imshow('Resultado', blend)
cv2.waitKey()
