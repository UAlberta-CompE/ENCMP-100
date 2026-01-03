##
#  Simulates the rolling of 5 dice and draws the face of each die in a
#  graphics window.
#

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from random import randint

# Define a constant for die size.
DIE_SIZE = 60

def main():
   ax = configureWindow(DIE_SIZE*7)
   rollDice(ax, DIE_SIZE)
   while rollAgain():
      ax = configureWindow(DIE_SIZE*7)
      rollDice(ax, DIE_SIZE)

## Prompt the user whether to roll again or quit.
#  @return True if the user wants to roll again
#
def rollAgain():
   userInput = input("Press the Enter key to roll again or enter Q to quit: ")
   if userInput.upper() == "Q":
      return False
   else:
      return True

## Create and configure the graphics window.
#  @param winSize the vertical and horizontal size of the window
#  @return the canvas used for drawing
#
def configureWindow(winSize):
   plt.axis([0, winSize-1, 0, winSize-1])
   ax = plt.gca()
   ax.invert_yaxis()
   ax.xaxis.set_visible(False)
   ax.yaxis.set_visible(False)
   ax.set_aspect('equal', 'box')
   ax.set_facecolor((0, 128/255, 0))
   return ax

## Simulates the rolling of 5 dice and draws the face of each die on a graphical
#  canvas in two rows with 3 dice in the first row and 2 in the second row.
#  @param ax the graphical canvas on which to draw the dice
#  @param size an integer indicating the dimensions of a single die
#
def rollDice(ax, size):
   # Set the initial die offset from the upper-left corner of the canvas.
   xOffset = size
   yOffset = size
   # Roll and draw each of five dice.
   for die in range(5):
      dieValue = randint(1, 6)
      drawDie(ax, xOffset, yOffset, size, dieValue)
      if die == 2:
         xOffset = size*2
         yOffset = size*3
      else:
         xOffset = xOffset + size*2
   plt.show()

## Draws a single die on the canvas.
#  @param ax the canvas on which to draw the die
#  @param x the x-coordinate for the upper-left corner of the die
#  @param y the y-coordinate for the upper-left corner of the die
#  @param size an integer indicating the dimensions of the die
#  @param dieValue an integer indicating the number of dots on the die
#
def drawDie(ax, x, y, size, dieValue):
   # The size of the dot and positioning will be based on the size of the die.
   dotSize = size/10
   offset1 = dotSize*2
   offset2 = dotSize*5
   offset3 = dotSize*8
   # Draw the rectangle for the die.
   fill = 'white'
   outline = 'black'
   ax.add_patch(Rectangle([x, y], size, size,
                          facecolor=fill, edgecolor=outline, linewidth=2))
   # Set the color used for the dots.
   color = 'black'
   # Draw the center dot or middle row of dots, if needed.
   if dieValue == 1 or dieValue == 3 or dieValue == 5:
      ax.add_patch(Circle([x + offset2, y + offset2], dotSize,
                          facecolor=color, edgecolor=color, linewidth=1))
   elif dieValue == 6:
      ax.add_patch(Circle([x + offset1, y + offset2], dotSize,
                          facecolor=color, edgecolor=color, linewidth=1))
      ax.add_patch(Circle([x + offset3, y + offset2], dotSize,
                          facecolor=color, edgecolor=color, linewidth=1))
   # Draw the upper-left and lower-right dots, if needed.
   if dieValue >= 2:
      ax.add_patch(Circle([x + offset1, y + offset1], dotSize,
                          facecolor=color, edgecolor=color, linewidth=1))
      ax.add_patch(Circle([x + offset3, y + offset3], dotSize,
                          facecolor=color, edgecolor=color, linewidth=1))
   # Draw the lower-left and upper-right dots, if needed.
   if dieValue >= 4:
      ax.add_patch(Circle([x + offset1, y + offset3], dotSize,
                          facecolor=color, edgecolor=color, linewidth=1))
      ax.add_patch(Circle([x + offset3, y + offset1], dotSize,
                          facecolor=color, edgecolor=color, linewidth=1))

# Start the program.
main()
