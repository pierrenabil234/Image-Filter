import numpy as np
from sort import sort
def min_filter(size,img):
    ro, co = img.shape
    img_fil = np.zeros_like(img)

    for r in range(ro):
        for c in range(co):
            region = []
            for i in range(-size//2, size//2 + 1):
                for j in range(-size//2, size//2 + 1):
                    if r + i >= 0 and r + i < ro and c + j >= 0 and c + j < co:
                        region.append(img[r + i][c + j])
                    else:
                        region.append(0)

            region = sort(region)
            img_fil[r][c] = np.min(region)

    return img_fil