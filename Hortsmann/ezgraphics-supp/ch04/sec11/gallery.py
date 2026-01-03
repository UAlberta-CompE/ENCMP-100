##
#  This program arranges a collection of pictures into rows by lining
#  them up along the top edges and separating them with small gaps.
#

import matplotlib.pyplot as plt

GAP = 10
NUM_PICTURES = 20
MAX_WIDTH = 720

plt.axis([0, 749, 0, 749])  # Taller window to show all pictures
plt.gca().invert_yaxis()
plt.axis('off')

pic = plt.imread('picture1.gif')
plt.imshow(pic)

x = 0
y = 0
maxY = 0
for i in range(2, NUM_PICTURES + 1):
   maxY = max(maxY, pic.shape[0])
   previous = pic
   filename = 'picture%d.gif' % i
   pic = plt.imread(filename)
   x = x + previous.shape[1] + GAP
   if x + pic.shape[1] < MAX_WIDTH:
      plt.imshow(pic, extent=(x, x + pic.shape[1] - 1, y + pic.shape[0] - 1, y))
   else:
      x = 0
      y = y + maxY + GAP
      plt.imshow(pic, extent=(x, x + pic.shape[1] - 1, y + pic.shape[0] - 1, y))
      maxY = 0 # Start of new row

plt.show()
