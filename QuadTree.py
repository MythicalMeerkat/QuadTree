# Jeff Wilson

import cv2
from numpy import asarray

# Read .pgma image into Numpy Array
im = cv2.imread('baboon.pgma')
image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# Note to Self: Result of loading with cv2 is a Numpy Array!
print('Type of Image after CV2: ' + str(type(image)) + '\n')


# Summarize shape
print('Shape of Image after CV2: ' + str(image.shape) + '\n')

# Printing Raw Data of Image
print('Printing Data of Image: \n')
print(image)

# TODO: Look into creating recursive split function. Refer to GM.



