# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:33:48 2024

@author: Acer
"""

import cv2
import numpy as np

# Membaca citra grayscale
img = cv2.imread('C:/Users/Acer/OneDrive/Pictures/Camera Roll/WIN_20230413_21_23_57_Pro.jpg', 100)

# Deteksi tepi menggunakan Canny
canny = cv2.Canny(img, 100, 200)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()