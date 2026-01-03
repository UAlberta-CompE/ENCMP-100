##
#  This program draws three colored rectangles on a canvas.
#

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create the window and access the canvas.
plt.axis([0, 399, 0, 199])
ax = plt.gca()
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Draw on the canvas.
ax.add_patch(Rectangle([0, 10], 200, 10, facecolor='red'))
ax.add_patch(Rectangle([0, 30], 300, 10, facecolor='green'))
ax.add_patch(Rectangle([0, 50], 100, 10, facecolor='blue'))

# Wait for the user to close the window.
plt.show()
