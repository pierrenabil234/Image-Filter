import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QWidget, QFileDialog, QComboBox, QLineEdit
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
import numpy as np


from avg import avg_filter
from gauss import gauss_filter
from lap import laplacian_filter_N4
from max import max_filter
from median import median_filter
from min import min_filter
from robert_cross import robert_cross_filter
from sobel import sobel_filter
from unsharp import unsharp_mask
from histogram import make_histo
from histo_equal import equal
from histo_match import match_histogram
from inter_nn import nn
from bilinear import bilinear_interpolation
from salt_and_pep import add_noise
from gaussian_noise import add_gaussian_noise
from uniform_noise import add_uniform_noise
from huffman import huffman_image_compression,huffman_image_decompression
from fourier import fourier_transform,fourier_inverse



class PhotoFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Project")
        self.setGeometry(100, 100, 1200, 400)  

        # Widgets
        self.image_label_original = QLabel(self)
        self.image_label_original.setAlignment(Qt.AlignCenter)

        self.image_label_reference = QLabel(self)
        self.image_label_reference.setAlignment(Qt.AlignCenter)

        self.image_label_filtered = QLabel(self)
        self.image_label_filtered.setAlignment(Qt.AlignCenter)

        self.upload_button = QPushButton("Upload Photo")
        self.upload_button.clicked.connect(self.upload_photo)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.update_photo)

        self.filter_button = QPushButton("Apply Filter")
        self.filter_button.clicked.connect(self.apply_filter)

        self.ref_upload_button = QPushButton("Upload Reference Photo")
        self.ref_upload_button.clicked.connect(self.upload_reference_photo)
        self.ref_upload_button.setEnabled(False)

        self.dimensions_input = QLineEdit()  
        self.dimensions_input.setMaximumWidth(300)
        self.dimensions_input.setPlaceholderText("Enter dimensions")

        self.K = QLineEdit() 
        self.K.setMaximumWidth(300)
        self.K.setPlaceholderText("K")

        self.filter_combobox = QComboBox()
        self.filter_combobox.addItems(["Median", "Max", "Min", "Average", "Gaussian", "Laplacian", "Unsharp", "Sobel", "Robert Cross", "Histogram",
                                        "Histogram equalization", "Histogram matching","Nearest Neighbor", "Salt and Pepper","Gaussian Noise",
                                        "Uniform Noise", "Bilinear","Compression","Decompression","fourier transform","fourier inverse"])

        # Layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.upload_button)
        left_layout.addWidget(self.image_label_original)

        center_layout = QVBoxLayout()
        center_layout.addWidget(self.ref_upload_button)
        center_layout.addWidget(self.dimensions_input)
        center_layout.addWidget(self.K)
        center_layout.addWidget(self.image_label_reference)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.filter_combobox)
        right_layout.addWidget(self.filter_button)
        right_layout.addWidget(self.refresh_button)
        right_layout.addWidget(self.image_label_filtered)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Image paths
        self.image_path = ""
        self.ref_image_path = ""

    def update_photo(self):
        if self.image_path:
            pixmap = self.image_label_filtered.pixmap()
            if pixmap:
                temp_image_path = "temp_filtered_image.png"
                pixmap.save(temp_image_path)
                self.image_path = temp_image_path
                self.image_label_original.setPixmap(pixmap.scaled(self.image_label_original.size(), Qt.KeepAspectRatio))

    def upload_photo(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        if file_dialog.exec_():
            self.image_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(self.image_path)
            self.image_label_original.setPixmap(pixmap.scaled(self.image_label_original.size(), Qt.KeepAspectRatio))
            self.ref_upload_button.setEnabled(True)

    def upload_reference_photo(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        if file_dialog.exec_():
            self.ref_image_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(self.ref_image_path)
            self.image_label_reference.setPixmap(pixmap.scaled(self.image_label_reference.size(), Qt.KeepAspectRatio))

    def apply_filter(self):
        if self.image_path:
            image = cv2.imread(self.image_path, 0)
            ro, co = image.shape
            compressed_image=""
            root= None
            image = cv2.resize(image, (100, 100))
            filter_type = self.filter_combobox.currentText()
            filtered_image = np.zeros_like(image, dtype=np.int64)
            tmp = np.zeros_like(image, dtype=np.int64)
            dimensions_text = self.dimensions_input.text()
            if not dimensions_text:
                self.dimensions_input.setText("3")
                dimensions = 3
            else:
                dimensions = int(dimensions_text)
                
            K_text = self.K.text()
            if not K_text:
                self.K.setText("1")
                K = 1
            else:
                K = int(K_text)

            if filter_type == "Median":
                filtered_image = median_filter(dimensions, image).astype(np.int64)
            elif filter_type == "Max":
                filtered_image = max_filter(dimensions, image).astype(np.int64)
            elif filter_type == "Min":
                filtered_image = min_filter(dimensions, image).astype(np.int64)
            elif filter_type == "Average":
                filtered_image = avg_filter(dimensions, image).astype(np.int64)
            elif filter_type == "Gaussian":
                filtered_image = gauss_filter(dimensions, image).astype(np.int64)
            elif filter_type == "Laplacian":
                filtered_image = laplacian_filter_N4(image).astype(np.float32)
            elif filter_type == "Unsharp":
                tmp = avg_filter(dimensions, image).astype(np.float32)
                filtered_image = unsharp_mask(image, K, tmp).astype(np.uint8)
            elif filter_type == "Sobel":
                filtered_image = sobel_filter(image).astype(np.int64)
            elif filter_type == "Robert Cross":
                filtered_image = robert_cross_filter(image).astype(np.int64)
            elif filter_type == "Histogram":
                make_histo(image)
            elif filter_type == "Histogram equalization":
                filtered_image = equal(image).astype(np.int64)
            elif filter_type == "Histogram matching":
                self.ref_upload_button.setEnabled(True)
                if self.ref_image_path:
                    self.ref_upload_button.setEnabled(True)
                    ref_image = cv2.imread(self.ref_image_path, 0)
                    filtered_image = match_histogram(image, ref_image).astype(np.int64)
            elif filter_type == "Nearest Neighbor":
                filtered_image=np.zeros_like((ro*dimensions,co*dimensions))
                filtered_image = nn(image, (ro*dimensions), (co*dimensions)).astype(np.int64)
            elif filter_type == "Bilinear":
                filtered_image=np.zeros_like((ro*dimensions,co*dimensions))
                filtered_image = np.array(bilinear_interpolation(image, ro * dimensions, co * dimensions)).astype(np.int64)
            elif filter_type == "Salt and Pepper":
                filtered_image = add_noise(image,K).astype(np.int64)
            elif filter_type == "Gaussian Noise":
                filtered_image = add_gaussian_noise(image,K).astype(np.int64)
            elif filter_type == "Uniform Noise":
                filtered_image = add_uniform_noise(image,K).astype(np.int64)
            elif filter_type=="Compression":
                self.original_shape = image.shape
                compressed_image, self.root, self.huffman_codes= huffman_image_compression(image)
                print(compressed_image)
            elif filter_type=="Decompression":
                filtered_image = huffman_image_decompression(compressed_image, self.root,self.original_shape)
            elif filter_type=="fourier transform":
                filtered_image=fourier_transform(image)
            elif filter_type=="fourier inverse":
                filtered_image=fourier_inverse(image)

        filtered_image_normalized = ((filtered_image - np.min(filtered_image)) / (np.max(filtered_image) - np.min(filtered_image))) * 255
        filtered_image_normalized = filtered_image_normalized.astype(np.uint8)  
        height, width = filtered_image.shape
        bytes_per_line = width
        q_image = QImage(filtered_image_normalized.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(q_image)
        self.image_label_filtered.setPixmap(pixmap.scaled(self.image_label_filtered.size(), Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoFilterApp()
    window.show()
    sys.exit(app.exec_())
