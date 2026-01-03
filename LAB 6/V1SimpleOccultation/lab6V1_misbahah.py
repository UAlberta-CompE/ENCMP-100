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
# Student name: Misbah Ahmed Nauman (90%)
# Student CCID: misbahah
# Others: Muhammad Hamiz Awais (10%, got help for the occultSquare() and gerchbergSaxton() function)
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



# Purpose: Simulates an optical system, including occultation and phase aberration correction, for a coronagraph
# Arguments: im (of type list) that stores a grayscale image representing the object to be observed
#            width (of type integer): that stores the width of the occulting square that will be applied to the image
# Returns: (im, Dphi) (a tuple) containing the processed image after occultation and the phase aberration correction term Dphi
# Side Effects: Modifies the input image 'im' by applying occultation to create a black square in the center and 
#               generates random phase aberration 'Dphi' used for simulating phase aberrations in the optical system
def opticalSystem(im,width):
    im = occultSquare(im,width)
    (IMa,IMp) = dft2(im)
    rng = np.random.default_rng(12345)
    imR = rng.random(im.shape)
    (_,Dphi) = dft2(imR)
    im = idft2(IMa,IMp-Dphi)
    return (im,Dphi)



# Purpose: computes the coordinates for the side-lengths, and uses this to create a square in the middle of the image
# Arguments: im (of type list) that stores a grayscale image representing the object to be observed
#            width (of type integer): that stores the width of the occulting square that will be applied to the image
# Returns: processed image
# Side Effects: none
def occultSquare(im, width):
    horizontal_start = int((im.shape[0] - width) / 2)
    horizontal_end = horizontal_start + width
    vertical_start = int((im.shape[1] - width) / 2)
    vertical_end = vertical_start + width
    im[horizontal_start:horizontal_end, vertical_start:vertical_end] = 0
    
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



# Purpose: Implements the Gerchberg-Saxton algorithm to iteratively correct phase aberrations in an image
# Arguments: im (of type list): the input grayscale image with phase aberrations
#            maxIters (of type integer): the maximum number of iterations to perform for phase correction
#            Dphi (of type float): the total phase aberration term to be corrected
# Returns: images ( of type list) representing the iterative corrections of the input image
# Side Effects: modifies the input image 'im' during each iteration to correct phase aberrations
def gerchbergSaxton(im, maxIters, Dphi):
    (IMa,IMp) = dft2(im)
    images = []
    
    for k in range(maxIters+1):
        print("Iteration %d of %d" % (k,maxIters))
        im = idft2(IMa, IMp + (Dphi / (maxIters + 1) * k))
        images.append(im)
    return images



# Purpose: saves each iterative image as frames in .png format in the working directory
# Arguments: images (of type list) containing generated images after the iteration
# Returns: none
# Side Effects: saves the images to a file and outputs a plot for each iterative image 
def saveFrames(images):
    shape = (images[0].shape[0],images[0].shape[1],3)
    image = np.zeros(shape,images[0].dtype)
    maxIters = len(images)-1
    
    for k in range(maxIters+1):
        image[:,:,0] = images[k]
        image[:,:,1] = images[k]
        image[:,:,2] = images[k]
        plt.imshow(image)
        
        # Adding title to image to match provided output
        plt.title("Iteration " + str(k) + " of " + str(maxIters))
        
        # Removing x-axis and y-axis to match provided output
        plt.xticks([])
        plt.yticks([])
        
        plt.savefig('coronagraph'+str(k)+'.png')
        plt.show()



main()
