# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:23:43 2024

@author: Acer
"""

import cv2
import numpy as np

# Membaca citra grayscale
img = cv2.imread('C:/Users/Acer/OneDrive/Pictures/Camera Roll/WIN_20230413_21_23_57_Pro.jpg', 100)

# Mendefinisikan kernel Roberts
kernel_x = np.array([[1, 0], [0, -1]])
kernel_y = np.array([[0, 1], [-1, 0]])

# Konvolusi dengan kernel
roberts_x = cv2.filter2D(img, cv2.CV_64F, kernel_x)
roberts_y = cv2.filter2D(img, cv2.CV_64F, kernel_y)

# Menghitung magnitudo gradien
mag = np.sqrt(roberts_x**2 + roberts_y**2)

# Normalisasi
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
mag = mag.astype(np.uint8)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Roberts Cross', mag)
cv2.waitKey(0)
cv2.destroyAllWindows()