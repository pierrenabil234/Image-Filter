import numpy as np

class Node:
    def __init__(self, pixel=None, frequency=0):
        self.pixel = pixel
        self.frequency = frequency
        self.left = None
        self.right = None

def calculate_frequency(image):
    frequency = {}
    for row in image:
        for pixel in row:
            if pixel in frequency:
                frequency[pixel] += 1
            else:
                frequency[pixel] = 1
    return frequency

def build_huffman_tree(frequency):
    nodes = [Node(pixel, freq) for pixel, freq in frequency.items()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        nodes.append(merged)
    return nodes[0]


def generate_huffman_codes(root, current_code="", codes={}):
    if codes is None:
        codes={}
    if root is None:
        return codes
    if root.pixel is not None:
        codes[root.pixel] = current_code
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)
    return codes


def compress_image(image, huffman_codes):
    compressed_image = ""
    for row in image:
        for pixel in row:
            compressed_image += huffman_codes[pixel]
    return compressed_image


def decompress_image(compressed_image, root,width):
    current_node = root
    decompressed_image = []
    row = []
    for bit in compressed_image:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.pixel is not None:
            row.append(current_node.pixel)
            current_node = root
            if len(row) == width: 
                decompressed_image.append(row)
                row = []
    return decompressed_image


def huffman_image_compression(image):
    frequency = calculate_frequency(image)
    print(frequency)
    root = build_huffman_tree(frequency)
    huffman_codes = generate_huffman_codes(root)
    compressed_image = compress_image(image, huffman_codes)
    print(compressed_image)
    return compressed_image, root, huffman_codes

def huffman_image_decompression(compressed_image, root, width):
    decompressed_image = decompress_image(compressed_image, root, width)
    return decompressed_image
