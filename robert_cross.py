import numpy as np
def robert_cross_filter(img):
    row, col = img.shape
    img_fil = np.zeros_like(img, dtype=np.float32)
    r1=np.array([[1,0],
                 [0,-1]],dtype=np.int8)
    r2=np.array([[0,1],
                 [-1,0]],dtype=np.int8)
#robert cross 3obara 3an el 2 kernels dol madrobin fel image we ba5od el sqrt(kernel**2)


    for r in range(row):
        for c in range(col):
            t1=t2=0
            for i in range(-1, 1):
                for j in range(-1, 1):
                    if 0 <= r + i < row and 0 <= c + j < col:
                        t1 += img[r + i][c + j] * r1[i + 1][j + 1]
                        t2 += img[r + i][c + j] * r2[i + 1][j + 1]

            gradient_magnitude = np.sqrt(t1**2 + t2**2)
            img_fil[r][c] = gradient_magnitude

    return img_fil
