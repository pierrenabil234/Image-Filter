import numpy as np
import matplotlib.pyplot as plt

def match_histogram(img, ref_img):

    H = np.zeros(256, dtype=int)
    for pixel_value in img.flatten():
        H[pixel_value] += 1
        intensity1=np.arange(0,256,1)

    ref_H = np.zeros(256, dtype=int)
    for pixel_value in ref_img.flatten():
        ref_H[pixel_value] += 1
        intensity2=np.arange(0,256,1)


    cdf=np.zeros_like(H)
    sum=0
    for i in range(len(H)):
        sum+=H[i]
        cdf[i]=sum
    
    cdf_normalized = cdf / float(cdf.max())

    ref_cdf=np.zeros_like(ref_H)
    sum=0
    for i in range(len(ref_H)):
        sum+=ref_H[i]
        ref_cdf[i]=sum
    ref_cdf_normalized = ref_cdf / float(ref_cdf.max())


    mapping_function = np.interp(cdf_normalized, ref_cdf_normalized, np.arange(256))


    matched_img = mapping_function[img].astype(int)


 
    match_H = np.zeros(256, dtype=int)
    for pixel_value in matched_img.flatten():
        match_H[pixel_value] += 1
        intensity3=np.arange(0,256,1)



    fig, axs = plt.subplots(1, 3, figsize=(16, 6))

    axs[0].bar(intensity1, H, color='red', width=0.5)
    axs[0].set_xlabel('Intensity')
    axs[0].set_ylabel('Frequency')
    axs[0].set_title('Original Histogram')

    axs[1].bar(intensity2, ref_H, color='yellow', width=0.5)
    axs[1].set_xlabel('Intensity')
    axs[1].set_ylabel('Frequency')
    axs[1].set_title('Refrenced Histogram')

    axs[2].bar(intensity3, match_H, color='blue', width=0.5)
    axs[2].set_xlabel('Intensity')
    axs[2].set_ylabel('Frequency')
    axs[2].set_title('Matched Histogram')
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()

    return matched_img

# Example usage:
# Load your images 'img' and 'ref_img' here
# matched_img = match_histogram(img, ref_img)
