import math
#using opencv3
import cv2
import numpy as np

def Representational(r, g, b):
    x = 0.2990
    y = 0.2870
    z = 0.1140
    
    return (x * r + y * g + z * b)


def calculate(img):
    
    b, g, r = cv2.split(img)
    pixelAt = Representational(r, g, b)
    print(pixelAt)
    return pixelAt


def main():
    # Loading images (orignal image and compressed image)
    
    orignal_image = cv2.imread('orignal_image.png', 1)
    compressed_image = cv2.imread('compressed_image.png', 1)

    # Getting image height and width
    height, width = orignal_image.shape[:2]

    orignalPixelAt = calculate(orignal_image)
    compressedPixelAt = calculate(compressed_image)

    diff = orignalPixelAt - compressedPixelAt
    error = np.sum(np.abs(diff) ** 2)

    error = error / (height * width)

    # MSR = error_sum/(height*width)
    P_SNR = -(10 * math.log10(error / (255 * 255)))

    print("PSNR value = {}".format(P_SNR))


if __name__ == '__main__':
    main()
