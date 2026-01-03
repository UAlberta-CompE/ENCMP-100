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
# Student name:
# Student CCID:
# Others:
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
    (im,Dphi,mask) = opticalSystem(im,300)
    (images,errors) = gerchbergSaxton(im,10,Dphi,mask)
    saveFrames(images,errors)
# Purpose: This function loads an image from a file.
# Input: A string name representing the filename of the image.
# Output: A 2D numpy array im representing the grayscale image.
# Side effects: None.
def loadImage(name):
    im = plt.imread(name)/255
    if len(im.shape) > 2:
        im = (im[:,:,0]+im[:,:,1]+im[:,:,2])/3
    im[im < 0] = 0
    im[im > 1] = 1
    return im

# Purpose: This function applies an optical system to an image.
# Input: A 2D numpy array im representing the grayscale image 
# and an integer width.
# Output: A tuple (im,Dphi,mask), where im is the modified image, Dphi is the 
# phase of the Fourier transform of a random image, and mask is a boolean mask 
# indicating the occulted pixels.
# Side effects: None.
def opticalSystem(im,width):
    (im,mask) = occultCircle(im,width)
    (IMa,IMp) = dft2(im)
    rng = np.random.default_rng(12345)
    imR = rng.random(im.shape)
    (_,Dphi) = dft2(imR)
    im = idft2(IMa,IMp-Dphi)
    return (im,Dphi,mask)

# Purpose: This function occults a circular region in the center of an image.
# Input: A 2D numpy array im representing the grayscale image and an integer 
# width.
# Output: A tuple (im, mask), where im is the modified image and mask is a 
# boolean mask indicating the occulted pixels.
# Side effects: None.
def occultCircle(im,width):
    xpixels, ypixels = im.shape
    mask = np.full(im.shape, False)
    for row in range(xpixels):
        for col in range(ypixels):
            # Note to TA: while writing this code, I didn't know what name to 
            # assign these varriables, so I just called them 'Dan' and emily
            # I would rename these to x-distance and y-distance, but I've
            # Chosen to keep them as is, because it's funny. Hope this 
            # brightens your day
            
            dan = xpixels//2-row
            emily = ypixels//2-col
            #This the equation of a circle btw (math was useful for once)
            if dan**2 + emily**2 <= (width//2)**2:  
                im[row,col] = 0    
                mask[row,col] = True
    return (im, mask)

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

# Purpose: This function applies the Gerchberg-Saxton algorithm to an image.
# Input: A 2D numpy array im representing the grayscale image, an integer
# maxIters representing the maximum number of iterations, a 2D numpy array Dphi
# representing the phase of the Fourier transform of a random image, and a
# boolean mask mask indicating the occulted pixels.
# Output: Two lists images and errors, where images contains the images at
# each iteration and errors contains the sum-square error at each iteration.
# Side effects: Prints the current iteration number to the console.
def gerchbergSaxton(im,maxIters,Dphi,mask):
    (IMa,IMp) = dft2(im)
    images = []
    errors = []
    for k in range(maxIters+1):
        print("Iteration %d of %d" % (k,maxIters))
        im = idft2(IMa,IMp+(k/maxIters)*Dphi)
        images.append(im)
        errors.append(occultError(mask, im))
    return images, errors

# Purpose: This function computes the sum-square error of the occulted
#  pixels in an image.
# Input: A boolean mask mask indicating the occulted pixels and a 2D numpy
# array im representing the grayscale image.
# Output: A float error representing the sum-square error.
# Side effects: None.
def occultError(mask, im):
    error = np.sum((im[mask])**2)
    return error
   
# Purpose: This function saves the images and errors at each
# iteration to a file.
# Input: Two lists images and errors, where images contains the images
# at each iteration and errors contains the sum-square error at each iteration.
# Output: None.
# Side effects: Saves the images and errors to a file and plots the error
# as a function of the iteration number. The plot is displayed in
# the console and saved to a file.
def saveFrames(images,errors):
    shape = (images[0].shape[0],images[0].shape[1],3)
    image = np.zeros(shape,images[0].dtype)
    maxIters = len(images)-1
    maxError = np.max(errors)
    for k in range(maxIters+1):
        image[:,:,0] = images[k]
        image[:,:,1] = images[k]
        image[:,:,2] = images[k]
        plt.plot(range(k+1), errors[0:k+1], color = 'red')
        plt.title("Coronagraph Simulation")
        plt.xlabel("Iteration")
        plt.ylabel("Sum-Square Error")
        plt.xlim([0,maxIters])
        plt.imshow(image, extent = [0, maxIters + 1, 0, maxError])
        plt.gca().set_aspect(maxIters/maxError)
        plt.savefig('coronagraph'+str(k)+'.png')
        plt.show()

main()