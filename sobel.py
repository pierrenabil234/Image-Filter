import numpy as np
def sobel_filter(img):
    row, col = img.shape
    img_fil = np.zeros_like(img, dtype=np.float32)
    s1 = np.array([[-1,0, 1],
                    [-2,0 , 2],
                    [-1,0 , 1]], dtype=np.int8)

    s2=np.array([[1,2,1],
                 [0,0,0],
                 [-1,-2,-1]], dtype=np.int8)

#nfs klam robert cross bas kernel mo5tlfa

    for r in range(row):
        for c in range(col):
            t1=t2=0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= r + i < row and 0 <= c + j < col:
                        t1 += img[r + i][c + j] * s1[i + 1][j + 1]
                        t2 += img[r + i][c + j] * s2[i + 1][j + 1]

            gradient_magnitude = np.sqrt(t1**2 + t2**2)
            img_fil[r][c] = gradient_magnitude

    return img_fil
