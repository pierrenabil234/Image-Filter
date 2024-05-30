import numpy as np
import cv2
import matplotlib.pyplot as plt
def laplacian_filter_N4(img):
    row, col = img.shape
    img_fil = np.zeros_like(img, dtype=np.float32)
    kernel = np.array([[1, 1, 1],
                       [1, -8, 1],
                       [1, 1, 1]], dtype=np.int8)


    for r in range(row):
        for c in range(col):
            total = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= r + i < row and 0 <= c + j < col:
                        total += img[r + i][c + j] * kernel[i + 1][j + 1]

            img_fil[r][c] = total
    return img_fil
