# Jeff Wilson

import cv2
import numpy

import warnings
warnings.filterwarnings("ignore")


def split(imageArr, x, y, width, height, var_threshold):
    # Number of Pixels in the quadrant
    # pixels = (height - x) * (width - y)
    pixels = imageArr[x:x+width, y:y+height].size

    # Calculate the Mean value of the Pixels in the Quadrant
    mean = (numpy.mean(imageArr[x:x+width, y:y+height]))

    # Calculate the Variance of the Quadrant
    variance = numpy.var(imageArr[x:x+width, y:y+height])

    if pixels <= 1:
        # Image Processing/Output
        return None
    if variance <= var_threshold:
        imageArr[x:x+width, y:y+height] = mean
        print("Replacing Pixels in Quad!")
        print(imageArr[x:x+width, y:y+height])
    else:
        split(imageArr, x, y, width//2, height//2, var_threshold)  # Top Left
        # width = 512
        # height = 512
        split(imageArr, x + width//2, y, width // 2, height // 2, var_threshold)  # Top Right
        # width = 512
        # height = 512
        split(imageArr, x, y + width//2, width // 2, height // 2, var_threshold)  # Bottom Left
        # width = 512
        # height = 512
        split(imageArr, x + width//2, y + height//2, width // 2, height // 2, var_threshold)  # Bottom Right
        # width = 512
        # height = 512


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

# Start Quad Tree Process
split(image, 0, 0, 512, 512, variance_threshold)

# Image Processing/Output
print('Printing Image! \n')
filename = "result_baboon_%d.pgm" % (variance_threshold)
cv2.imwrite(filename, image)
