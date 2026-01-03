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
# Student name: Muhammad Hamiz Awais
# Student CCID: awais3
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
#
# nm
data = [656.460,486.271,434.1692,410.2892, 397.1198, 389.0166, 383.6485] 
nist = np.array(data)
n = len(nist)

## MODEL SETUP

#electron mass
me = 9.1093837e-31

#fundamental_charge
e = 1.602176634e-19

#permittivity of free space 
e0 = 8.85418782e-12

#Planck constant
h = 6.62607015e-34

#speed of light
c = 299792458

#proton mass
mp = 1.6726219e-27


#equation
rydberg = (me * e**4) / (8 * e0**2 * h**3 * c)

#correction to rydberg equation
corrected_rydberg = rydberg * (mp / (mp + me))

print("Rydberg constant:", int(corrected_rydberg) , "m" + chr(8315) + chr(185)) 

#rounded_rydberg = int(corrected_rydberg) ##print(rounded_rydberg)


## SIMULATION DATA

#
nf = input("Final state (nf): ")
nf = int(nf)
ni = np.arange(nf+1,nf+n+1)

#equation 2
wavelength = 1 / (corrected_rydberg *((1/nf**2) - 1/ni**2))

#wavelength in nm
wavelength_in_nm = wavelength / 1e-9


#plot
plt.plot(ni,nist,'bx' , label="NIST DATA")
plt.plot(ni , wavelength_in_nm, 'r.' , label="Bohr Model")
plt.legend()
plt.title("Hydrogen Emission Spectrum")
plt.xlabel("Initial State (ni)")
plt.ylabel("Wavelength (nm)")


plt.grid(True)

plt.show()


## ERROR ANALYSIS

#difference between NIST wavelengths and Bohr wavelengths
difference = data - wavelength_in_nm

#worst-case error
worst_case = np.max(np.abs(difference))
float(worst_case)
print("Worst-case Error:", "%.3f" % worst_case , "nm")
#bar graph
plt.bar(ni, difference , color="m" ,label= "NIST - Bohr")
plt.title("Hydrogen Emission Spectrum")
plt.legend()
plt.xlabel("Initial State (ni)")
plt.ylabel("Wavelength (nm)")
plt.show()