import matplotlib.pyplot as plt

plt.axis([0, 749, 0, 349])
plt.gca().invert_yaxis()

pic = plt.imread('picture1.gif')
plt.imshow(pic)

plt.show()
