"""Compression ratio"""

# Distortion in image
# Mean squared error


from math import log10, sqrt
import numpy as np
import cv2


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def MSE(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    return mse


def main():
    original_img_size = 3.43 * 1024  # KB
    compressed_img_size = 863.6  # KB

    print(f"Compression Ratio = {original_img_size / compressed_img_size}")
    original = cv2.imread("ivp.jpg")
    compressed = cv2.imread("ivp_converted_to_jpeg.jpg", 1)
    value = PSNR(original, compressed)
    value1 = MSE(original, compressed)
    print(f"PSNR value is {value} dB")
    print(f"MSE value id {value1} dB")
