## HSPECTRUM  Quantum Chemistry and the Hydrogen Emission Spectrum
#
# The periodic table is central to chemistry. According to Britannica,
# "Detailed understanding of the periodic system has developed along with
# the quantum theory of spectra and the electronic structure of atoms,
# beginning with the work of Bohr in 1913." In this lab assignment, a
# University of Alberta student explores the Bohr model's accuracy in
# predicting the hydrogen emission spectrum, using observed wavelengths
# from a US National Institute of Standards and Technology database.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Misbah Ahmed Nauman
# Student CCID: misbahah
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
import numpy as np
import matplotlib.pyplot as plt



## EXPERIMENT DATA

#List of observed wavelengths in the visible band of the hydrogen emission spectrum in nanometers (nm)
data = [656.460, 486.271, 434.1692, 410.2892, 397.1198, 389.0166, 383.6485]

#Converting data to a NumPy array
nist = np.array(data)

#Storing size of nist in n
n = len(nist)



## MODEL SETUP

#Declaring RYDBERG as a constant of type float with units of 1/m
RYDBERG = 1.0973732e7 

#Assigning values to each physical constant
ELECTRON_MASS = 9.1093837e-31 # float with units of Kilograms (Kg)
FUNDAMENTAL_CHARGE = 1.6021766e-19 # float with units of Coulombs (C)
PERMITTIVITY_OF_FREE_SPACE = 8.8541878e-12 # float with units of Force-per-meter (F/m)
PLANCK_CONSTANT = 6.6260702e-34 # float with units of Joules-second (J*s)
SPEED_OF_LIGHT = 299792460 # integer with units Metre-per-second (m/s)
PROTON_MASS = 1.6726219e-27 # float with units if Kilograms (Kg)

#Assigning an expression for R of type float using the declared constants
R = ((ELECTRON_MASS) * (FUNDAMENTAL_CHARGE ** 4)) / ((8) * (PERMITTIVITY_OF_FREE_SPACE ** 2) * (PLANCK_CONSTANT ** 3) * (SPEED_OF_LIGHT))

#Correction for R to account for a finite nuclear mass
R = R * ((PROTON_MASS) / (PROTON_MASS + ELECTRON_MASS)) 

print("Rydberg constant:", int(R), "m" + chr(8315) + chr(185))



## SIMULATION DATA

#Requesting input from user to the final quantum state
nf = input("Final state (nf): ")

#Converting inputted string value to integer and storing in nf
nf = int(nf)

#Creating an array of initial quantum states (ni) 
ni = np.arange(nf+1, nf+n+1)

#Assigning an expression for wavelength using the BOHR model formula where R is the Rydberg constant, nf is the final quantum state and ni is the initial quantum state
wavelength_in_meters = (1) / ((R) * (((1) / (nf ** 2)) - ((1) / (ni ** 2)))) # unit in metres (m)

#Converting the wavelength 
wavelength_in_nanometers = wavelength_in_meters * 1000000000 # unit in nanometers (nm)

#Plotting data points of nist in a blue cross 
plt.plot(ni, nist, 'bx', label = "NIST data")

#Plotting the data points of Bohr model in a red dot
plt.plot(ni, wavelength_in_nanometers, 'r.', label = "Bohr model")

#Labelling the x-axis, y-axis and the title of the graph
plt.xlabel("Initial state (ni)")
plt.ylabel("Wavelength (nm)")
plt.title("Hydrogen Emission Spectrum")

#Displaying the legend
plt.legend()

#Displaying the grid
plt.grid(True)

#Displaying the plot
plt.show()



## ERROR ANALYSIS

#Calculating the difference in wavelengths between the NIST and Bohr model
difference = data - wavelength_in_nanometers # float with units of Nanometers (nm)

#Calcultaing the worst-case error between the NIST and Bohr model
worst_case_error = np.max(np.abs(difference)) # integer with units of Nanometers (nm)
print("Worst-case error: %0.3f" % worst_case_error, "nm")

#Plotting the data points of NIST-Bohr wavelengths (in nm) against Initial state
plt.bar(ni, difference, color = "m", label = "NIST-Bohr")

#Labelling the x-axis, y-axis and the title of the bar graph
plt.xlabel("Initial state (ni)")
plt.ylabel("Wavelength (nm)")
plt.title("Hydrogen Emission Spectrum")

#Displaying the legend
plt.legend()

#Displaying the plot
plt.show()