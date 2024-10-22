# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:28:11 2024

@author: Acer
"""

import cv2
import numpy as np

# Membaca citra grayscale
img = cv2.imread('C:/Users/Acer/OneDrive/Pictures/Camera Roll/WIN_20230413_21_23_57_Pro.jpg', 100)

# Menggunakan fungsi cv2.Scharr untuk deteksi tepi
sobelx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
sobely = cv2.Scharr(img, cv2.CV_64F, 0, 1)

# Menghitung magnitudo gradien
mag = np.sqrt(sobelx**2 + sobely**2)

# Normalisasi
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
mag = mag.astype(np.uint8)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Scharr Magnitude', mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()