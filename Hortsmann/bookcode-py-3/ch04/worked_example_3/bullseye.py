##
#  Draws a target with a bull's eye using the number of rings 
#  specified by the user.
#

from ezgraphics import GraphicsWindow

# Define constant variables.
MIN_NUM_RINGS = 2
MAX_NUM_RINGS = 10
RING_WIDTH = 25
TARGET_OFFSET = 10

# Obtain number of rings in the target.
numRings = int(input("Enter # of rings in the target: "))
while numRings < MIN_NUM_RINGS or numRings > MAX_NUM_RINGS :
   print("Error: the number of rings must be between", 
          MIN_NUM_RINGS, "and", MAX_NUM_RINGS)
   numRings = int(input("Re-enter # of rings in the target: "))
      
# Determine the diameter of the outermost circle. It has to be drawn first.
diameter = (numRings + 1) * RING_WIDTH * 2
   
# Determine the size of the window based on the size of the outer circle.
winSize = diameter + 2 * TARGET_OFFSET

# Create the graphics window and get the canvas.
win = GraphicsWindow(winSize, winSize)
canvas = win.canvas()

# Use a light gray background for the canvas.
canvas.setBackground("light gray")

# Draw the rings, alternating between black and white.
x = TARGET_OFFSET
y = TARGET_OFFSET
for ring in range(numRings) :
   if ring % 2 == 0 :
      canvas.setColor("black")
   else :
      canvas.setColor("white")      
   canvas.drawOval(x, y, diameter, diameter)
   
   diameter = diameter - 2 * RING_WIDTH
   x = x + RING_WIDTH
   y = y + RING_WIDTH

# Draw the bull's eye in red.
canvas.setColor("red")
canvas.drawOval(x, y, diameter, diameter)

win.wait()

