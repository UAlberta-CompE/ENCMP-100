import matplotlib.pyplot as plt

GAP = 10
NUM_PICTURES = 5  # Temporarily set to 5 for testing step 6.
MAX_WIDTH = 720

plt.axis([0, 749, 0, 349])
plt.gca().invert_yaxis()

pic = plt.imread('picture1.gif')
plt.imshow(pic)

x = 0
maxY = 0
for i in range(2, NUM_PICTURES + 1):
   maxY = max(maxY, pic.shape[0])
   previous = pic
   filename = 'picture%d.gif' % i
   pic = plt.imread(filename)
   x = x + previous.shape[1] + GAP
   if x + pic.shape[1] < MAX_WIDTH:
      plt.imshow(pic, extent=(x, x + pic.shape[1] - 1, pic.shape[0] - 1, 0))
   else:
      y = maxY + GAP
      plt.imshow(pic, extent=(0, pic.shape[1] - 1, y + pic.shape[0] - 1, y))

plt.show()
