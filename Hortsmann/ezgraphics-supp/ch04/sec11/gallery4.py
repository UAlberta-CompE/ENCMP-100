import matplotlib.pyplot as plt

GAP = 10

plt.axis([0, 749, 0, 349])
plt.gca().invert_yaxis()

pic = plt.imread('picture1.gif')
plt.imshow(pic)

pic2 = plt.imread('picture2.gif')
x = pic.shape[1] + GAP
plt.imshow(pic2, extent=(x, x + pic2.shape[1] - 1, pic2.shape[0] - 1, 0))

pic3 = plt.imread('picture3.gif')
x = x + pic2.shape[1] + GAP
plt.imshow(pic3, extent=(x, x + pic3.shape[1] - 1, pic3.shape[0] - 1, 0))

plt.show()
