import numpy as np

def nn(img, m, n):
    ro, co = img.shape
    new_img = np.zeros((m, n), dtype=img.dtype)
    for r in range(ro):
        for c in range(co):
            for row in range(r * m // ro, (r + 1) * m // ro):
                for col in range(c * n // co, (c + 1) * n // co):
                    new_img[row, col] = img[r, c]
    return new_img
