import numpy as np
def add_uniform_noise(image,high, low=0):
    row, col = image.shape
    noisy_image = np.zeros_like(image, dtype=np.float32)
    for i in range(row):
        for j in range(col):
            noise = np.random.uniform(low, high)
            noisy_pixel = image[i, j] + noise
            if noisy_pixel < 0:
                noisy_pixel = 0
            elif noisy_pixel > 255:
                noisy_pixel = 255
            noisy_image[i, j] = noisy_pixel
    return noisy_image.astype(np.uint8)