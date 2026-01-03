
# Hydrogen Emission Spectrum Simulation

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# EXPERIMENT DATA
# List of measured wavelengths in nanometers (nm)
experimental_data = [656.460, 486.271, 434.1692, 410.2892,
                     397.1198, 389.0166, 383.6485]  
# Convert the list to a NumPy array for further calculations
nist_data = np.array(experimental_data)
# Calculate the length of the data (number of data points)
n = len(nist_data)  

# MODEL SETUP
# Define various physical constants used in the calculations

# Rydberg constant in 1/m
rydberg = 1.0973732e7  

# Mass of an electron in kilograms (Kg)
electron_mass = 9.10938188e-31  

# Fundamental charge in Coulombs (C)
fundamental_charge = 1.602176634e-19  

# Permittivity of free space in F/m
permittivity_of_free_space = 8.8541878128e-12

# Planck constant in J·s
planck_constant = 6.62607015e-34  

# Speed of light in meters per second (m/s)
speed_of_light = 299792458  

proton_mass = 1.67262192 * 10**-27

# Calculate the Rydberg constant using the defined constants
rydberg = (electron_mass * (fundamental_charge ** 4)) / (8 * (permittivity_of_free_space ** 2) * (planck_constant ** 3) * speed_of_light)

scale_factor = (proton_mass)/(proton_mass + electron_mass)

rydberg = scale_factor * rydberg

# Print the calculated Rydberg constant
print("Rydberg constant:", int(rydberg), "m"+chr(8315)+chr(185))

# SIMULATION DATA
# Prompt the user for the final quantum state (nf)
nf = input("Final State (nf):")
# Convert the user input to an integer
nf = int(nf)  
# Create an array of quantum states (ni) starting from nf+1 to nf+n
ni = np.arange(nf + 1, nf + n + 1)  

# Calculate the corresponding wavelengths using the Bohr model formula
wavelength = 1 / (rydberg * (1 / nf ** 2 - (1 / ni ** 2)))
# Convert wavelengths from meters to nanometers
wavelength = wavelength * 1000000000  

# Create a plot to visualize the data
# Plot NIST data points in blue 'x' markers
plt.plot(ni, nist_data, 'bx', label='NIST Data')  
# Plot Bohr model data in red
plt.plot(ni, wavelength, 'r.', label='Bohr Model')

# Customize the plot with labels and grid
plt.grid(True)
plt.ylabel('Wavelength (nm)')
plt.xlabel('Initial state (ni)')
plt.title('Hydrogen Emission Spectrum')
# Display the legend indicating data series
plt.legend()  
# Display the plot
plt.show()

# ERROR ANALYSIS
error = experimental_data - wavelength
plt.bar(ni, error, width=0.3, color='magenta', label='NIST-Bohr')
plt.legend()
plt.ylabel('Difference (nm)')
plt.xlabel('Initial state (ni)')
plt.title('Difference Between Experimental Data and Simulation Model')
print('Worst-case error:', '%.3f' % max(abs(error)), 'nm')
