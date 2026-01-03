##
#  This program creates a graphics window with a rectangle. It provides the
#  template used with all of the graphical programs used in the book.
#

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create the window and access the canvas.
plt.axis([0, 399, 0, 399])
ax = plt.gca()
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Draw on the canvas.
ax.add_patch(Rectangle([5, 10], 20, 30))

# Wait for the user to close the window.
plt.show()
