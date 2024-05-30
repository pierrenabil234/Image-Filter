import numpy as np

def fourier_transform(img):
    ro = img.shape[0]
    co = img.shape[1]
    img_fil = np.zeros((ro, co), dtype=np.complex128)
    for i in range(ro):
        for w in range(co):
            val = 0
            for r in range(ro):
                for c in range(co):
                    val += img[r, c] * np.exp(-2j * np.pi * ((r * i / ro) + (c * w / co)))
            img_fil[i, w] = val
    return img_fil

import numpy as np

def fourier_inverse(image_fil):
    ro = image_fil.shape[0]
    co = image_fil.shape[1]
    img_reconstructed = np.zeros_like(image_fil, dtype=np.complex128)
    j = 1j
    for i in range(ro):
        for w in range(co):
            val = 0
            for r in range(ro):
                for c in range(co):
                    val2 = 2 * np.pi * ((r * i / ro) + (c * w / co))
                    val += image_fil[r, c] * np.exp(j * val2)
            img_reconstructed[i, w] = val / (ro * co)
    return img_reconstructed.real  # Returning only the real part since the image should be real


