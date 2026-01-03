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
# Others: Ali Abdullah (10%, helped with the occultCircle() function and saveFrames() function)
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
    (im, Dphi, mask) = opticalSystem(im, 300)
    (images, errors) = gerchbergSaxton(im, 10, Dphi, mask)
    saveFrames(images, errors)



def loadImage(name):
    im = plt.imread(name)/255
    if len(im.shape) > 2:
        im = (im[:,:,0]+im[:,:,1]+im[:,:,2])/3
    im[im < 0] = 0
    im[im > 1] = 1
    return im



# Purpose: simulates an optical system, including occultation and phase aberration correction, for a coronagraph
# Arguments: im (of type list): input grayscale image representing the object to be observed
#            width (of type integer): width of the occulting square that will be applied to the image
# Returns: im (of type list): processed image after occultation and phase aberration correction
#          Dphi (of type float): phase aberration correction term used for simulating phase aberrations in the optical system
#          mask (of type list): boolean mask indicating the pixels occulted by the square
# Side Effects: modifies the input image 'im' by applying occultation to create a black square in the center and
#               generates random phase aberration 'Dphi' used for simulating phase aberrations in the optical system
def opticalSystem(im, width):
    (im, mask) = occultCircle(im, width)
    (IMa, IMp) = dft2(im)
    rng = np.random.default_rng(12345)
    imR = rng.random(im.shape)
    (_, Dphi) = dft2(imR)
    im = idft2(IMa, IMp-Dphi)
    
    return (im, Dphi, mask)



# Purpose: occults a circle at the center of the input image, creating a black region
# Arguments: im (of type list): input grayscale image
#            width (of type integer): width of the circle to occult, in pixels
# Returns: im (of type list): image with the circle occulted
#          mask (of type list): boolean mask indicating the pixels occulted by the circle
# Side Effects: modifies the input image 'im' by creating a black circle at its center and 
#               generates a mask identifying the occulted pixels in the image 
def occultCircle(im, width):
    (x_pixels, y_pixels) = im.shape
    mask = np.full(im.shape, False)
    
    for row in range(x_pixels):
        for column in range(y_pixels):
            x_distance = x_pixels // 2 - row
            y_distance = y_pixels // 2 - column
            
            # Using the equation of a circle
            if ((x_distance ** 2) + (y_distance ** 2)) <= ((width // 2) ** 2):  
                im[row,column] = 0    
                mask[row,column] = True
                
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



# Purpose: implements the Gerchberg-Saxton algorithm to iteratively correct phase aberrations in an image
# Arguments: im (of type list): input grayscale image with phase aberrations
#            maxIters (of type integer): maximum number of iterations to perform for phase correction
#            Dphi (of type float): total phase aberration term to be corrected
#            mask (of type list): boolean mask indicating the pixels occulted by the circle
# Returns: images (list of arrays): iterative corrections of the input image
#          errors (list of floats): list of errors computed for each iteration
# Side Effects: modifies the input image 'im' during each iteration to correct phase aberrations and
#               appends errors to the 'errors' list
def gerchbergSaxton(im, maxIters, Dphi, mask):
    (IMa,IMp) = dft2(im)
    images = []
    errors = []
    
    for k in range(maxIters+1):
        print("Iteration %d of %d" % (k,maxIters))
        im = idft2(IMa, IMp + (k / maxIters) * Dphi)
        images.append(im)
        errors.append(occultError(mask, im))
        
    return images, errors



# Purpose: computes the error in the Gerchberg-Saxton algorithm by summing the squared values of image 
#          entries where the corresponding mask entries are True
# Arguments: mask (of type list): boolean mask indicating the pixels occulted by the circle
#            im (of type list): input grayscale image with phase aberrations
# Returns: error (of type float): total error computed for the given image and mask
# Side effects: none
def occultError(mask, im):
    error = np.sum((im[mask]) ** 2)
    return error



# Purpose: saves each iterative image as frames in .png format in the working directory and plots the error
#          progression over iterations
# Arguments: images (list of arrays): list of generated images after each iteration
#            errors (list of floats): list of error values for each iteration
# Returns: none
# Side Effects: saves the images to a file and outputs a plot for each iterative image showing the error progression
def saveFrames(images, errors):
    shape = (images[0].shape[0],images[0].shape[1],3)
    image = np.zeros(shape,images[0].dtype)
    maxIters = len(images)-1
    maxError = np.max(errors)
    
    for k in range(maxIters+1):
        image[:,:,0] = images[k]
        image[:,:,1] = images[k]
        image[:,:,2] = images[k]
        
        # Creating plot of image, adding titles, and adding axis names to match provided output
        plt.plot(range(k+1), errors[0:k+1], color = 'red')
        plt.title("Coronagraph Simulation")
        plt.xlabel("Iteration")
        plt.ylabel("Sum-Square Error")
        plt.xlim([0, maxIters])
        
        # Displaying the image with proper aspect ratio to match provided output
        plt.imshow(image, extent = [0, maxIters + 1, 0, maxError])
        plt.gca().set_aspect(maxIters / maxError)
        
        plt.savefig('coronagraph'+str(k)+'.png')
        plt.show()



main()