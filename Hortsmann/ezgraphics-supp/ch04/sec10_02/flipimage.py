##
#  This program creates a new flipped version of a GIF image.
#
import matplotlib.pyplot as plt
import numpy as np

# Load the original image.
filename = input("Enter the name of the image file: ")
origImage = plt.imread(filename)

# Create an empty image that will contain the new flipped image.
width = origImage.shape[1]
height = origImage.shape[0]
newImage = np.zeros(origImage.shape, origImage.dtype)

# Iterate over the image and copy the pixels to the new image to
# produce the flipped image.
newRow = height - 1
for row in range(height):
   for col in range(width):
      newCol = col
      pixel = origImage[row, col]
      newImage[newRow, newCol] = pixel
   newRow = newRow - 1

# Save the new image with a new name.
plt.imsave('flipped-' + filename, newImage)
