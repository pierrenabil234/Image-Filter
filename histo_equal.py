import numpy as np
import matplotlib.pyplot as plt


def equal(img):
    H = np.zeros(256, dtype=int)
    for pixel_value in img.flatten():
        H[pixel_value] += 1
        intensity1=np.arange(0,256,1)


    cdf=np.zeros_like(H)
    sum=0
    for i in range(len(H)):
        sum+=H[i]
        cdf[i]=sum
    
    cdf_normalized = cdf / float(np.sum(H))
    mapping_function = (2**8 - 1) * cdf_normalized

    equalized_img = mapping_function[img]
    equalized_img = np.round(equalized_img).astype(np.uint8)

    equalized_H = np.zeros(256, dtype=int)
    for pixel_value in equalized_img.flatten():
        equalized_H[pixel_value] += 1
        intensity=np.arange(0,256,1)

    fig, axs = plt.subplots(1, 2, figsize=(16, 6))
    equal_img = np.zeros_like(img, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            equal_img[i, j] = mapping_function[img[i, j]]

    intensity = np.arange(256)

    axs[0].bar(intensity1, H, color="red", width=0.5)
    axs[0].set_xlabel("Intensity")
    axs[0].set_ylabel("Frequency")
    axs[0].set_title("Original Histogram")

    axs[1].bar(intensity, equalized_H, color='blue', width=0.5)
    axs[1].set_xlabel('Intensity')
    axs[1].set_ylabel('Frequency')
    axs[1].set_title('Equalized Histogram')
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()
    return equal_img
