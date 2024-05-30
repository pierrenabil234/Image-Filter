import numpy as np
def add_gaussian_noise(image,sigma, mean=0):
    row, col = image.shape
    noisy_image = np.zeros_like(image)
    noise_values = []  

    for i in range(row):
        for j in range(col):
            ranv1 = np.random.rand()
            ranv2 = np.random.rand()
            
            u = np.sqrt(-2 * np.log(ranv1)) * np.cos(2 * np.pi * ranv2)
            v = np.sqrt(-2 * np.log(ranv1)) * np.sin(2 * np.pi * ranv2)

            noise = u * sigma + mean
            noise_values.append(noise)  
            noisy_pixel = image[i, j] + noise
            if noisy_pixel < 0:
                noisy_pixel = 0
            elif noisy_pixel > 255:
                noisy_pixel = 255

            noisy_image[i, j] = int(noisy_pixel) 
    return noisy_image 