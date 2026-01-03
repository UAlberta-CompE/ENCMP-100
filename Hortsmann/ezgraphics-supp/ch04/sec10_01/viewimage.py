##
#  This program provides a simple image viewer that loads an image from
#  a file displays it in a window.
#
import matplotlib.pyplot as plt

# Load the image from the file.
filename = input("Enter the name of the image file: ")
image = plt.imread(filename)

# Display it in a window and wait for the user to close the window.
plt.imshow(image)
plt.axis('off')
plt.show()
