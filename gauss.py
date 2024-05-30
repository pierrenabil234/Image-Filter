import numpy as np
from sort import sort
def gauss_filter(size,img):
    ro, co = img.shape
    img_fil = np.zeros_like(img, dtype=np.float16)

    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]], dtype=np.float16)
    #el kernel bta3t el gauss
    kernel = kernel / 16
    #kol cell* 1/16
    for r in range(ro):
        for c in range(co):
            total = 0.0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= r + i < ro and 0 <= c + j < co:
                        total += img[r + i][c + j] * kernel[i + 1][j + 1]

            img_fil[r][c] = total
            

    return img_fil
