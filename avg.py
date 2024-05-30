import numpy as np
from sort import sort
def avg_filter(size,img):
    ro, co = img.shape
    img_fil = np.zeros_like(img)

    for r in range(ro):
        for c in range(co):
            #loop 3la el sora dimensions
            region = []
            for i in range(-size//2, size//2 + 1):
                for j in range(-size//2, size//2 + 1):
                    #loop el kernel,, law el kernel 3*3 hatb2a mn -1-->1 dah 3lshan awl row
                    if r + i >= 0 and r + i < ro and c + j >= 0 and c + j < co:
                        #b3ml check eni gowa el sora
                        region.append(img[r + i][c + j])
                    else:
                        region.append(0)

            region = sort(region)
            img_fil[r][c] = np.average(region)
            #el pixel babdlha bi avg el filter

    return img_fil