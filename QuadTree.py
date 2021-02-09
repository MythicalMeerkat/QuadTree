# Jeff Wilson

import cv2
import numpy


def split(imageArr, x, y, width, height, var_threshold):
    # Number of Pixels in the quadrant
    # pixels = (height - x) * (width - y)
    pixels = imageArr.size

    # Split imageArr into Quadrant
    # print(imageArr)

    # Calculate the Mean value of the Pixels in the Quadrant
    mean = (numpy.mean(imageArr, axis=(0, 1)))

    # Calculate the Variance of the Quadrant
    variance = numpy.var(imageArr)

    if pixels <= 1:
        # Image Processing/Output
        return None
    if variance <= var_threshold:
        imageArr[0:width, 0:height] = mean
        print('Filling Pixels in Quadrant! \n')
        print('Amount of Pixels in Quadrant: ' + str(pixels) + '\n')
        print('Variance of the Quadrant: ' + str(variance) + '\n')
        print('Mean of Pixel Values: ' + str(mean) + '\n')
        print(imageArr)
    else:
        split(imageArr[x:x+width//2, y:y+height//2], x, y, width//2, height//2, var_threshold)  # Top Left
        split(imageArr[x+width//2:x+width, y:y+height//2], x + width//2, y, width // 2, height // 2, var_threshold)  # Top Right
        split(imageArr[x:x+width//2, y+height//2:y+height], x, y + width//2, width // 2, height // 2, var_threshold)  # Bottom Left
        split(imageArr[x+width//2:x+width, y+height//2:y+height], x + width//2, y + height//2, width // 2, height // 2, var_threshold)  # Bottom Right
        print(imageArr)


# Client Input
variance_threshold = input('Enter the variance threshold: ')
variance_threshold = int(variance_threshold)

# Read .pgma image into Numpy Array
image = cv2.imread('baboon.pgma', -1)
image_copy = cv2.imread('baboon.pgma', -1)


# Note to Self: Result of loading with cv2 is a Numpy Array!
print('--- Image Properties --- \n')
print('Type: ' + str(type(image)) + '\n')


# Summarize shape
print('Shape: ' + str(image.shape) + '\n')

# Printing Raw Data of Image
# print('Image Data: \n')
# print(image)

# Start Quad Tree Process
split(image, 0, 0, 256, 256, variance_threshold)

# Image Processing/Output
print('Printing Image! \n')
cv2.imwrite('result_baboon.pgm', image)









