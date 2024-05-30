import numpy as np
import matplotlib.pyplot as plt

def make_histo(img):
    H = np.zeros(256, dtype=int)
    for pixel_value in img.flatten():
        H[pixel_value] += 1
        intensity=np.arange(0,256,1)
    # print(intensity)
    # print(H)
    plt.bar(intensity,H,color="red",width=0.5)
    plt.xlabel("intensity")
    plt.ylabel("Frequenc")
    plt.show()