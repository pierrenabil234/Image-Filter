import random
import cv2

def add_noise(img,max):
	row, col = img.shape
	total_pixels = row * col
	min_pixels = total_pixels // 100  # 1% of total pixels
	max_pixels = total_pixels // max    
	number_of_pixels = random.randint(min_pixels, max_pixels)#b5tar 3dd el ml7/ white noise
	for i in range(number_of_pixels):
		y_coord = random.randint(0, row - 1)
		x_coord = random.randint(0, col - 1)
		#random position
		img[y_coord][x_coord] = 255 #7atena ml7
	number_of_pixels = random.randint(300, 10000) #b5tar 3dd el felfl/black noise
	for i in range(number_of_pixels):
		y_coord = random.randint(0, row - 1)
		x_coord = random.randint(0, col - 1)
		img[y_coord][x_coord] = 0#7atena felel
	return img
