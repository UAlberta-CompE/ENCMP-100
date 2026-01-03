##HIDE
##OUT out.png
## 
#
# This module is a simplified version of the ezgraphics module (v2.1) 
# for use with CodeCheck. Instead of using Tk to display graphics and
# images in a GUI window, it builds and saves the result in a PNG image.
# 
# Version: 2.1.2
#
# Changes since version 2.1
# Fixed the setFill, setColor, and setOutline canvas methods to work with
# color names that contain blank spaces. tkinter allows blank spaces in 
# the names, but PIL does not.
#
# Changes since version 2.1.1
# Fixed the setPixel method to work with floating-point RGB values. If a
# floating point number given, it is truncated to an integer. tkinter
# correctly handles floating-point values, but PIL does not.
#
from PIL import Image, ImageDraw, ImageColor, ImageFont

OUTPUT_FILENAME = "out.png"

class GraphicsWindow :
  def __init__(self, width = 400, height = 400) :
    if width is None and height is None :
      width = 400
      height = 400

    self._canvas = GraphicsCanvas(self, width, height) 
    
  def canvas(self) :
    return self._canvas
    
  def wait(self) :
    img = self._canvas._pilImage
    img.save(OUTPUT_FILENAME)
  
  def setTitle(self, title) :
    pass
  
  def isValid(self) :
    return True
    
  def hide(self) :
    pass
  
  def show(self) :
    pass
  
  def close(self) :
    pass
  
  def quit(self) :
    pass
  
  def getMouse(self) :
    return (0, 0)
    
  def getKey(self) :
    return ""
    
  def sleep(self, msTime) :
    pass
  
  def menu(self) :
    return None
    
  def showMenu(self) :
    pass
  
  def hideMenu(self) :
    pass
  
  def showStatus(self) :
    pass
  
  def hideStatus(self) :
    pass
  
  def setStatus(self, text="") :
    pass
  
  def configStatus(self, **options) :
    pass
  
  def enableEvents(self, *events) :
    pass
  
  def clearEvents(self, *events) :
    pass
  
  def setEventHandler(self, handler) :
    pass
  
  def setTimer(self, msTime) :
    pass
  
  def clearTimer(self) :
    pass    
  
  def onMenuSelect(self, event) :
    pass
    
  def onMouseMove(self, event) :
    pass
    
  def onMouseDrag(self, event) :
    pass
  
  def onMouseDown(self, event):
    pass
 
  def onMouseUp(self, event):
    pass
  
  def onKeyPress(self, event) :
    pass
  
  def onAlarm(self, event) :
    pass
  
  
class GraphicsCanvas :
  def __init__(self, win, width, height) :
   
     # The win argument is ignored in the codecheck version.
    self._win = win
   
     # Maintain the options used for drawing objects and text.
    self._polyOpts = {"outline" : (0, 0, 0), "width" : 1, "dash" : None, "fill" : None}
    self._arcStyle = "pieslice"
    self._textOpts = {"justify" : "left", "anchor" : "nw",
                      "fill" : "black",
                      "font" : ("helvetica", 10, "normal")}
    self._font = None
    self._bgColor = (255, 255, 255)    
                      
     # Create the PIL image.
    self._pilImage = Image.new("RGB", (width, height), (255, 255,255))
    self._pilDraw = ImageDraw.Draw(self._pilImage)
    
  ## Changes the height of the canvas.
  #
  def setHeight(self, size):
    if type(size) != int or size <= 0 :
      raise GraphicsParamError( "The window height must be >= 1." )
    if size < self.height() :
      self._shrinkImage(self.width(), size)
    else :
      self._enlargeImage(self.width(), size)

  ## Changes the width of the canvas.
  #
  def setWidth(self, size):    
    if type(size) != int or size <= 0 :
      raise GraphicsParamError("The window width must be >= 1.")
    if size < self.width() :
      self._shrinkImage(size, self.height())
    else :
      self._enlargeImage(size, self.height())

  def _shrinkImage(self, width, height) :
    self._pilImage = self._pilImage.crop((0, 0, width, height))
    self._pilDraw = ImageDraw.Draw(self._pilImage)
    
  def _enlargeImage(self, width, height) :
    oldImage = self._pilImage
    self._pilImage = Image.new("RGB", (width, height), (255, 255,255))
    self._pilImage.paste(oldImage, (0, 0))         
    self._pilDraw = ImageDraw.Draw(self._pilImage)
    
  ## Returns the height of the canvas.
  #
  def height(self):
    return self._pilImage.size[1]
  
  ## Returns the width of the canvas.
  #
  def width(self):
    return self._pilImage.size[0]
     
  ## Clears the canvas by removing all items previously drawn on it. 
  #
  def clear(self):
    width = self.width()
    height = self.height()
    self._pilImage = Image.new("RGB", (width, height), (255, 255,255))
    self._pilDraw = ImageDraw.Draw(self._pilImage)
   
  ## Sets the current background color of the canvas. (not used)
  #   
  def setBackground(self, red, green = None, blue = None) :
    if type(red) == int :
      color = "#%02X%02X%02X" % (red, green, blue) 
    elif type(red) != str :
      raise GraphicsParamError("Invalid color.")
    else :
      color = red

  ## Sets the fill color used when drawing new polygon shapes. 
  #    
  def setFill(self, red = None, green = None, blue = None) :
    if red is None :
      color = None
    elif type(red) == int :
      color = (red, green, blue)       
    elif type(red) != str :
      raise GraphicsParamError("Invalid color.")
    else :
      string = red.replace(" ", "")
      color = ImageColor.getrgb(string)
    self._polyOpts["fill"] = color
        
  ## Sets the outline color used when drawing new polygon shapes and the
  #
  def setOutline(self, red = None, green = None, blue = None) :
    if red is None :
      color = None
    elif type(red) == int :
      color = (red, green, blue)  
    elif type(red) != str :
      raise GraphicsParamError("Invalid color.")
    else :
      string = red.replace(" ", "")
      color = ImageColor.getrgb(string)
    self._polyOpts["outline"] = color
    self._textOpts["fill"] = color
     
  ## Sets both the fill and outline colors used when drawing shapes and text
  #  on the canvas. 
  #
  def setColor(self, red, green = None, blue = None) :
    if type(red) == int :
       color = (red, green, blue)
    elif type(red) != str :
       raise GraphicsParamError("Invalid color.")
    else :
       string = red.replace(" ", "")
       color = ImageColor.getrgb(string)
    self._polyOpts["outline"] = color
    self._polyOpts["fill"] = color
    self._textOpts["fill"] = color     
    
  ## Sets the width of lines drawn on the canvas. 
  #
  def setLineWidth(self, size):
    if type(size) != int or size <= 0 :
      raise GraphicsParamError("Invalid line width.")
    self._polyOpts["width"] = size
    if self._polyOpts["dash"] :
      self._polyOpts["dash"] = (4 * size, 4 * size)

  ## Sets the style used to drawn lines on the canvas. (not used) 
  #
  def setLineStyle(self, style):
    if style == "dashed" :
      width = self._polyOpts["width"]
      self._polyOpts["dash"] = (4 * width, 4 * width)
    else :
      self._polyOpts["dash"] = None


  ## Sets the style used when drawing an arc on the canvas. 
  #
  def setArcStyle(self, style) :
    if style not in ("pieslice", "chord", "arc") :
      raise GraphicsParamError("Invalid arc style.")
    self._arcStyle = "pieslice"
  
  ## Sets the font used to draw text on the canvas. 
  #  
  def setTextFont(self, family = None, style = None, size = None ):
    origFamily, origSize, origStyle = self._textOpts["font"]
    if family is None :
      family = origFamily    
    elif (family is not None and 
       family not in ('helvetica', 'arial', 'courier', 'times', 'times roman')) :
      raise GraphicsParamError("Invalid font family.")
      
    if style is None :
      style = origStyle    
    elif (style is not None and 
       style not in ('bold', 'normal', 'italic', 'bold italic')) :
      raise GraphicsParamError( "Invalid font style." )

    if size is None :
       size = origSize    
    elif size is not None and (type(size) != int or size <= 0) :
      raise GraphicsParamError( "Invalid font size." )
       
    self._textOpts["font"] = (family, size, style)     

  ## Sets the position that text is drawn in relation to a bounding box. 
  #
  def setTextAnchor(self, position):
    if position not in ('n', 's', 'e', 'w', 'nw', 'ne', 'sw', 'se', 'center') :
      raise GraphicsParamError( "Invalid anchor position." )       
    self._textOpts["anchor"] = position
          
  ## Sets the justification used to draw new multiline text on the canvas.
  #
  def setTextJustify(self, style):
    if style in ("left", "center", "right") :
      self._textOpts["justify"] = style
    else :
      raise GraphicsParamError("Invalid justification value.")
    
  ## Draws or plots a single point (pixel) on the canvas.
  #
  def drawPoint(self, x, y) :
    self._pilDraw.point((round(x), round(y), round(x+1), round(y)), 
                        fill=self._polyOpts["outline"])
    return 0    

  ## Draws a line segment on the canvas. 
  #
  def drawLine(self, x1, y1, x2, y2):
    self._pilDraw.line((round(x1), round(y1), round(x2), round(y2)), 
      fill=self._polyOpts["outline"],
      width=self._polyOpts["width"])
    return 0
  
  ## Draws an arrow or vector on the canvas. (Draws a line) 
  #
  def drawArrow(self, x1, y1, x2, y2) :
    return self.drawLine(x1, y1, x2, y2)
    
  ## Draws a rectangle on the canvas. 
  #
  def drawRect(self, x, y, width, height) :
    self._pilDraw.rectangle((round(x), round(y), 
                             round(x + width), round(y + height)), 
              outline=self._polyOpts["outline"], fill=self._polyOpts["fill"])
    return 0
  
  def drawRectangle(self, x, y, width, height) :
    return self.drawRect(x, y, width, height)
                       
  ## Draws a polygon on the canvas. 
  #
  def drawPoly(self, *coords):
    minCoords = 6
    
     # Unwrap the cooridinates which allows the method to accept individual 
     # vertices or a list of vertices.
    if len(coords) == 1 and (type(coords[0]) == list or type(coords[0]) == tuple) :
       expCoords = tuple(*coords)
    else :
       expCoords = coords
       
    if type(expCoords[0]) == list or type(expCoords[0]) == tuple :
      minCoords = 3
       
    if len(expCoords) < minCoords :
      raise GraphicsParamError("At least 3 vertices must be provided.")
      
    self._pilDraw.polygon(expCoords, 
              outline=self._polyOpts["outline"], fill=self._polyOpts["fill"])
    return 0
  
  ## The same as drawPoly().
  #
  def drawPolygon(self, *coords) :
    return self.drawPoly(*coords)
      
  ## Draws an oval on the canvas. 
  #
  def drawOval(self, x, y, width, height):
    self._pilDraw.ellipse((round(x), round(y), 
                           round(x + width), round(y + height)),
              outline=self._polyOpts["outline"], fill=self._polyOpts["fill"])
    return 0    
            
  ## Draws an arc or part of a circle on the canvas.
  #
  def drawArc(self, x, y, diameter, startAngle, extent) :
    x = round(x)
    y = round(y)
    diameter = round(diameter)
    startAngle = round(startAngle)
    extent = round(extent)

     # Tk draws arcs counter-clockwise, but PIL draws them clockwise.
    temp = startAngle
    endAngle = 360 - temp
    startAngle = 360 - temp - extent
    if self._arcStyle == "pieslice" :
      self._pilDraw.pieslice((x, y, x + diameter, y + diameter), 
                          startAngle, endAngle,
                          outline=self._polyOpts["outline"],
                          fill=self._polyOpts["fill"])
      
    elif self._arcStyle == "chord" :
      self._pilDraw.chord((x, y, x + diameter, y + diameter), 
                          startAngle, endAngle,
                          outline=self._polyOpts["outline"],
                          fill=self._polyOpts["fill"])
      
    elif self._arcStyle == "arc" :
      self._pilDraw.arc((x, y, x + diameter, y + diameter), 
                          startAngle, endAngle,        
                          fill=self._polyOpts["outline"])
    
    return 0
  
  ## Draws text on the canvas. 
  #  
  def drawText(self, x, y, text):
    self._pilDraw.text((round(x), round(y)), text,
                fill=self._textOpts["fill"],
                anchor=self._textOpts["anchor"],
                font=self._font)
    return 0
         
  ## Draws an image onto the canvas.
  #
  def drawImage(self, x, y = None, image = None) :
    if type(x) == GraphicsImage :
      image = x
      width = image.width()
      height = image.height()
      x = 0
      y = 0
      self._pilImage = Image.new("RGB", (width, height), (255, 255,255))
      self._pilDraw = ImageDraw.Draw(self._pilImage)
      
    self._pilImage.paste(image._pilImage, (round(x), round(y)))
    return 0
  
  def shiftItem(self, itemId, dx, dy) :
    pass
  
  def scaleItem(self, itemId, xScale, yScale, xOffset = None, yOffset = None) :
    pass
  
  def removeItem(self, itemId) :
    pass
  
  def showItem(self, itemId) :
    pass
  
  def hideItem(self, itemId) :
    pass
  
  def raiseItem(self, itemId, aboveId = None) :    
    pass

  def lowerItem(self, itemId, belowId = None) :
    pass
  
  def __contains__(self, itemId):
    return True
  
  def itemType(self, itemId) :
    return ""
    
  def items(self) :
    return []    
    
  def itemAbove(self, itemId) :
    return 0

  def itemBelow(self, itemId) :
    return 0
    
    
## This class defines a basic top level window that can display a
#  digital GraphicsImage.
#
class ImageWindow(GraphicsWindow) :
  
  ## Creates a new window for displaying images. This provides a quick
  #  way to display images without having to access and draw on the 
  #  canvas of a graphics window.
  #         
  def __init__(self) :
    super().__init__(None, None)
    self._imgId = None
    
  ## Displays an image in the window. The window is resized to fit tightly
  #  around the image.
  #  @param image  The GraphicsImage object containing the image to 
  #                be displayed.
  #
  def display(self, image = None) :
    if image is None : return
    canvas = self._canvas
    width = image.width()
    height = image.height()
    canvas._pilImage = Image.new("RGB", (width, height), (255, 255, 255)) 
    canvas._pilImage.paste(image, (0, 0))
    
## This class defines an RGB digital image that is contained within an
#  ImageWindow.
#
class GraphicsImage :
  
  ## Creates a new graphics image. 
  #
  def __init__(self, width = None, height = None) :
     # Create the photo image.
    if height is None and type(width) == str :
      filename = width
      self._pilImage = Image.open(filename)
      if self._pilImage.mode != "RGB" :
        self._pilImage = self._pilImage.convert("RGB")
    else :
      self._pilImage = Image.new("RGB", (width, height), (255, 255,255))
  
  ## Gets the width of the image in pixels.
  #  @return The width of the image.
  #
  def width(self) :
    return self._pilImage.size[0]

  ## Gets the height of the image in pixels.
  #  @return The width of the image.
  #
  def height(self) :
    return self._pilImage.size[1]

  ## Sets a pixel to a given RGB color.
  #
  def setPixel(self, row, col, *rgbColor) :
    if (row < 0 or row >= self.height() or
        col < 0 or col >= self.width()) : 
      return
    if len(rgbColor) == 1 :
      if type(rgbColor[0]) == str :
        if rgbColor[0][0] == "#" :
          color = ImageColor.getrgb(rgbColor)
        else :
          color = (0, 0, 0)
      else :
        color = tuple(*rgbColor)
    elif len(rgbColor) == 3 :
      color = rgbColor      
    col = round(col)
    row = round(row)
    color = (int(color[0]), int(color[1]), int(color[2]))    
    self._pilImage.putpixel((col, row), color)
  
  ## Returns a 3-tuple containing the RGB color of a given pixel.
  #
  def getPixel(self, row, col) :
    row = round(row)
    col = round(col)
    result = self._pilImage.getpixel((col, row))
    if type(result) == int :
      return (result, result, result)
    else :
      return result

  ## Returns the red component of the RGB color of a given pixel.
  #
  def getRed(self, row, col) :
    pixel = self.getPixel(row, col)
    return pixel[0]
    
  ## Returns the green component of the RGB color of a given pixel.
  #
  def getGreen(self, row, col) :
    pixel = self.getPixel(row, col)
    return pixel[1]
    
  ## Returns the blue component of the RGB color of a given pixel.
  #
  def getBlue(self, row, col) :
    pixel = self.getPixel(row, col)
    return pixel[2]
    
  ## Clears the image and removes all of the pixels but the size of the 
  #  image remains the same.
  #
  def clear(self) :
    width = self.width()
    height = self.height()    
    self._pilImage = Image.new("RGB", (width, height), (255, 255,255))
    
  ## Creates a duplicate copy of the image.
  #
  def copy(self) :
    image = GraphicsImage(10, 10)
    image._pilImage = self._pilImage.copy()
    return image
  
  ## Saves the digital image to a file in either the gif or ppm format.
  #
  def save(self, filename, format="gif") :
    if format not in ("gif", "ppm") :
      raise GraphicsParamError( "Invalid image format.")
    self._pilImage.save(filename, format=format)


# --- Defines special graphics exceptions that are raised when an error
# --- occurs in a GraphicsWindow method.

class GraphicsError(Exception) :
  def __init__( self, message ):
    super(GraphicsError, self).__init__( message )

class GraphicsObjError(GraphicsError) :
  def __init__( self ):
    super(GraphicsError, self).__init__( "Invalid object id." )

class GraphicsWinError(GraphicsError) :
  def __init__( self ):
    super(GraphicsWinError, self).__init__(
              "Operation can not be performed on a closed window." )

class GraphicsParamError(GraphicsError) :
  def __init__( self, message ):
    super(GraphicsParamError, self).__init__( message )
    
