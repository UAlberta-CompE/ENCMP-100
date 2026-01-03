import matplotlib.pyplot as plt

GAP = 10
NUM_PICTURES = 20

plt.axis([0, 749, 0, 349])
plt.gca().invert_yaxis()

pic = plt.imread('picture1.gif')
plt.imshow(pic)

x = 0
for i in range(2, NUM_PICTURES + 1):
   previous = pic
   filename = 'picture%d.gif' % i
   pic = plt.imread(filename)
   x = x + previous.shape[1] + GAP
   plt.imshow(pic, extent=(x, x + pic.shape[1] - 1, pic.shape[0] - 1, 0))

plt.show()
