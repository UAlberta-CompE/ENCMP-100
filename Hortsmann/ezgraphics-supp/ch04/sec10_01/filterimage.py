##
#  This program processes a digital image by creating a negative of
#  the original.
#
import matplotlib.pyplot as plt

# Load the image from the file.
filename = input("Enter the name of the image file: ")
image = plt.imread(filename)

# Process the image.
image = image.copy()
for row in range(image.shape[0]):
   for col in range(image.shape[1]):

      # Get the current pixel color.
      red = image[row, col, 0]
      green = image[row, col, 1]
      blue = image[row, col, 2]

      # Filter the pixel.
      newRed = 255 - red
      newGreen = 255 - green
      newBlue = 255 - blue

      # Set the pixel to the new color.
      image[row, col, 0:3] = (newRed, newGreen, newBlue)

# Display the image on screen.
plt.imshow(image)
plt.axis('off')
plt.show()

# Save the new image with a new name.
plt.imsave('negative-' + filename, image)
