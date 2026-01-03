## CORONASIMULATE  Simulate coronagraph and Gerchberg-Saxton algorithm
#
# A simulation of a coronagraph and the Gerchberg-Saxton algorithm, in the
# context of NASA's Roman Space Telescope, developed to help teach ENCMP
# 100 Computer Programming for Engineers at the University of Alberta. The
# program saves output figures to PNG files for subsequent processing.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Muhammad Hamiz Awais
# Student CCID: awais3
# Others: Ally Saad Muihuddin (5%)
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions will be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import matplotlib.pyplot as plt
import numpy as np

def main():
    im = loadImage('300_26a_big-vlt-s.jpg')
    (im,Dphi) = opticalSystem(im,300)
    images = gerchbergSaxton(im,10,Dphi)
    saveFrames(images)

def loadImage(name):
    im = plt.imread(name)/255
    if len(im.shape) > 2:
        im = (im[:,:,0]+im[:,:,1]+im[:,:,2])/3
    im[im < 0] = 0
    im[im > 1] = 1
    return im

def opticalSystem(im,width):
    im = occultSquare(im,width)
    (IMa,IMp) = dft2(im)
    rng = np.random.default_rng(12345)
    imR = rng.random(im.shape)
    (_,Dphi) = dft2(imR)
    im = idft2(IMa,IMp-Dphi)
    return (im,Dphi)

# Input parameters for the function are "im", a 2D array, and "width", an integer of value 300
# The function creates a square in the middle of the image by getting the coordinates of its side-lengths
# The side lengths are "width" apart from each other
def occultSquare(im,width):
    horizontal_start = int((im.shape[0]-width)/2)
    horizontal_end = horizontal_start + width
    vertical_start = int((im.shape[1]-width)/2)
    vertical_end = vertical_start + width
    im[horizontal_start:horizontal_end,vertical_start:vertical_end] = 0
    return im
    

# (IMa,IMp) = dft2(im) returns the amplitude, IMa, and phase, IMp, of the
# 2D discrete Fourier transform of a grayscale image, im. The image, a 2D
# array, must have entries between 0 and 1. The phase is in radians.
def dft2(im):
    IM = np.fft.rfft2(im)
    IMa = np.abs(IM)
    IMp = np.angle(IM)
    return (IMa,IMp)

# im = idft2(IMa,IMp) returns a grayscale image, im, with entries between
# 0 and 1 that is the inverse 2D discrete Fourier transform (DFT) of a 2D
# DFT specified by its amplitude, IMa, and phase, IMp, in radians.
def idft2(IMa,IMp):
    IM = IMa*(np.cos(IMp)+1j*np.sin(IMp))
    im = np.fft.irfft2(IM)
    im[im < 0] = 0
    im[im > 1] = 1
    return im
# This function has three input parameters 
# The fucntion iteratively improves the quality of the image 
# The function uses a formula for linear interpolation
def gerchbergSaxton(im,maxIters,Dphi):
    (IMa,IMp) = dft2(im)
    images = []
    for k in range(maxIters+1):
        print("Iteration %d of %d" % (k,maxIters))
        im = idft2(IMa, IMp + (Dphi / (maxIters+1)*k))
        images.append(im)
    return images

# The function saves the generated images after iteration as frames (saved as .png)
# It has the input parameter "images" which is the list of generated images after the iteration
# The function converts the image to grayscale, gives it a title, and removes the axes.
def saveFrames(images):
    shape = (images[0].shape[0],images[0].shape[1],3)
    image = np.zeros(shape,images[0].dtype)
    maxIters = len(images)-1
    for k in range(maxIters+1):
        # converts the image to grayscale
        image[:,:,0] = images[k]
        image[:,:,1] = images[k]
        image[:,:,2] = images[k]
        plt.imshow(image)
        # giving the image a title
        plt.title('Iterartion ' + str(k) + ' of ' + str(maxIters))
        # removing axes
        plt.xticks([])
        plt.yticks([])
        plt.savefig('coronagraph'+str(k)+'.png')
        plt.show()

main()
