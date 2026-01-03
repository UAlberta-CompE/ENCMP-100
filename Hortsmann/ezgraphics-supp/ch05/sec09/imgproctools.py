##
#
#
import numpy as np

## Creates and returns a new image that is the negative of the original.
#  @param image the source image
#  @return the new negative image
#
def createNegative(image):
   # Create a new image that is the same size as the original.
   newImage = np.zeros(image.shape, image.dtype)
   for row in range(image.shape[0]):
      for col in range(image.shape[1]):
         # Get the color of the pixel in the original image.
         red = image[row, col, 0]
         green = image[row, col, 1]
         blue = image[row, col, 2]
         # Filter the pixel.
         newRed = 255 - red
         newGreen = 255 - green
         newBlue = 255 - blue
         # Set the pixel in the new image to the new color.
         newImage[row, col, 0:3] = (newRed, newGreen, newBlue)
         newImage[row, col, 3:] = image[row, col, 3:]
   return newImage

## Creates and returns a new image in which the brightness levels of
#  all three color components are adjusted by a given percentage.
#  @param image the source image
#  @param amount the percentage by which to adjust the brightness
#  @return the new image
#
def adjustBrightness(image, amount):
   # Create a new image that is the same size as the original.
   newImage = np.zeros(image.shape, image.dtype)
   for row in range(image.shape[0]):
      for col in range(image.shape[1]):
         # Get the color of the pixel in the original image.
         red = image[row, col, 0]
         green = image[row, col, 1]
         blue = image[row, col, 2]
         # Adjust the brightness and cap the colors.
         newRed = int(red + red*amount)
         if newRed > 255:
            newRed = 255
         elif newRed < 0:
            newRed = 0
         newGreen = int(green + green*amount)
         if newGreen > 255:
            newGreen = 255
         elif newGreen < 0:
            newGreen = 0
         newBlue = int(blue + blue*amount)
         if newBlue > 255:
            newBlue = 255
         elif newBlue < 0:
            newBlue = 0
         # Set the pixel in the new image to the new color.
         newImage[row, col, 0:3] = (newRed, newGreen, newBlue)
         newImage[row, col, 3:] = image[row, col, 3:]
   return newImage

## Creates and returns a new image that results from flipping an original
#  image vertically.
#  @param image the source image
#  @return the new vertically flipped image
#
def flipVertically(image):
   # Create a new image that is the same size as the original.
   newImage = np.zeros(image.shape, image.dtype)
   # Flip the image vertically.
   newRow = image.shape[0] - 1
   for row in range(image.shape[0]):
      for col in range(image.shape[1]):
         newCol = col
         pixel = image[row, col]
         newImage[newRow, newCol] = pixel
      newRow = newRow - 1
   return newImage

## Flip the image diagonally at the main diagonal.
#  @param image the image to be transposed
#  @return the new transposed image
#
def flipDiagonally(image):
   # Create a new image whose dimensions are the opposite of the original.
   newShape = (image.shape[1], image.shape[0]) + image.shape[2:]
   newImage = np.zeros(newShape, image.dtype)
   # Transpose the image.
   for row in range(image.shape[0]):
      newCol = row
      for col in range(image.shape[1]):
         newRow = col
         pixel = image[row, col]
         newImage[newRow, newCol] = pixel
   return newImage

## Compares two images to determine if they are identical.
#  @param image1,image2 the two images to be compared
#  @return True if the images are identical,False otherwise
#
def sameImage(image1, image2):
   # Make sure the images are the same size.
   if image1.shape != image2.shape:
      return False
   # Compare the two images,pixel by pixel.
   for row in range(image1.shape[0]):
      for col in range(image1.shape[1]):
         pixel1 = image1[row, col]
         pixel2 = image2[row, col]
         # Compare the color components of corresponding pixels.
         for i in range(image1.shape[2]):
            if pixel1[i] != pixel2[i]:
               return False
   # Indicate the images are identical.
   return True
