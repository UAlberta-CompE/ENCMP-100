##
#  Draws a target with a bull's eye using the number of rings
#  specified by the user.
#

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Define constant variables.
MIN_NUM_RINGS = 2
MAX_NUM_RINGS = 10
RING_WIDTH = 25
TARGET_OFFSET = 10

# Obtain number of rings in the target.
numRings = int(input("Enter # of rings in the target: "))
while numRings < MIN_NUM_RINGS or numRings > MAX_NUM_RINGS:
   print("Error: the number of rings must be between",
         MIN_NUM_RINGS, "and", MAX_NUM_RINGS)
   numRings = int(input("Re-enter # of rings in the target: "))

# Determine the diameter of the outermost circle. It has to be drawn first.
diameter = (numRings + 1)*RING_WIDTH*2
radius = diameter/2

# Determine the size of the window based on the size of the outer circle.
winSize = diameter + 2*TARGET_OFFSET

# Create the graphics window and get the canvas.
plt.axis([0, winSize - 1 ,0, winSize - 1])
ax = plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_aspect('equal', 'box')
ax.invert_yaxis()

# Use a light gray background for the canvas.
lightgray = (0.827, 0.827, 0.827)
ax.set_facecolor(lightgray)

# Draw the rings, alternating between black and white.
x = TARGET_OFFSET
y = TARGET_OFFSET
for ring in range(numRings):
   if ring % 2 == 0:
      color = 'black'
   else:
      color = 'white'
   ax.add_patch(Circle([x + radius, y + radius], radius, facecolor=color))

   diameter = diameter - 2*RING_WIDTH
   radius = diameter/2
   x = x + RING_WIDTH
   y = y + RING_WIDTH

# Draw the bull's eye in red.
ax.add_patch(Circle([x + radius, y + radius], radius, facecolor='red'))

plt.show()
