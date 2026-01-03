## PERIHELION  Mercury's perihelion precession and general relativity
#
# In this lab assignment, a student completes a Python program to test with
# data an accurate prediction of Einstein’s theory, namely the perihelion
# precession of Mercury. Mercury’s orbit around the Sun is not a stationary
# ellipse, as Newton’s theory predicts when there are no other bodies. With
# Einstein’s theory, the relative angle of Mercury’s perihelion (position
# nearest the Sun) varies by about 575.31 arcseconds per century.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Misbah Ahmed Nauman (95%)
# Student CCID: misbahah
# Others: Ali Abdullah (5%) helped verbally with the refine() function
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



import numpy as np
from scipy import stats
import matplotlib.pyplot as plt



def main():
    data = loaddata('horizons_results')
    perihelion_data  = locate(data) # Perihelia
    selected_data = select(perihelion_data, 50, ('Jan', 'Feb', 'Mar'))
    data = refine(selected_data,'horizons_results')
    makeplot(data,'horizons_results')
    savedata(data,'horizons_results')



# Purpose: reads each line from filename.txt and converts them a list of dictionaries
# Arguments: filename (of type string) of a file to be read from 
# Side Effects: outputs lines of text to the Console to indicate progress
#               outputs if $$SOE line is missing from filename.txt               
# Returns: list of dictionaries that represent astronomical data
def loaddata(filename):
    file = open(filename+'.txt','r')
    lines = file.readlines()
    file.close()
    noSOE = True
    num = 0
    data = []
    for line in lines:
        if noSOE:
            if line.rstrip() == "$$SOE":
                noSOE = False
        elif line.rstrip() != "$$EOE":
            num = num+1
            if num % 10000 == 0:
                print(filename,":",num,"line(s)")
            datum = str2dict(line)
            data.append(datum)
        else:
            break # for
    if noSOE:
        print(filename,": no $$SOE line")
    else:
        print(filename,":",num,"line(s)")
    return data



# Purpose: Converts astronomical data of type string to a dictionary
# Arguments: line (of type string) contains csv values representing astronomical data
# Side Effects: none
# Returns: Dictionary with keys 'numdate', 'strdate', and 'coord' with their computated values
def str2dict(line):
    splitted_lines = line.split(',')
    
    numeric_date = float(splitted_lines[0].strip())
    
    # Replaces any occurence of 'A.D.' and '00:00:00.0000' with an empty string '' from string_date
    string_date = splitted_lines[1].replace('A.D. ', '').replace('00:00:00.0000', '').strip()
    
    # Storing the respective coordinates from strdate to variables and creating a tuple for the 3D coordinates
    x = float(splitted_lines[2].strip())
    y = float(splitted_lines[3].strip())
    z = float(splitted_lines[4].strip())
    coordinates = (x, y, z)
    
    return {'numdate': numeric_date, 'strdate': string_date, 'coord': coordinates}



# Purpose: locate and return perihelion data points
# Arguments: data1 (a list of dictionaries) containing astronomical data
# Side Effects: none
# Returns: a list of dictionaries representening perihelion data points
def locate(data1):
    dist = [] # Vector lengths
    for datum in data1:
        coord = np.array(datum['coord'])
        dot = np.dot(coord,coord)
        dist.append(np.sqrt(dot))
    data2 = []
    for k in range(1,len(dist)-1):
        if dist[k] < dist[k-1] and dist[k] < dist[k+1]:
            data2.append(data1[k])
    return data2



# Purpose: identify dates in data that meet criteria and return them as a list
# Arguments: data (a list of dictionaries) containing astronomical data
#            ystep (of type integer) used to select dates that meet criteria
#            month (a list of strings) used to select dates that meet criteria
# Side Effects: none
# Returns: all the dates (of type string, stored in a list) that meet the criteria
def select(data, ystep, month):
    output_data = []
    
    for line in data:
        date = line['strdate'].split('-')
        
        if (int(date[0]) % ystep == 0) and(date[1] in month):
            output_data.append(line)
        
    return output_data



# Purpose: creates a plot based on data and save it to a file. 
#          receives the slope of line of best fit and labels from the add2plot() function
# Arguments: data (a list of dictionaries) that contain data to be plotted
#            filename (of type string) represents the filename to save the plot as a png
# Side Effects: generates and saved a plot with the name "horizon_results.png"
# Returns: none
def makeplot(data,filename):
    (numdate,strdate,arcsec) = precess(data)
    
    # added labels for x and y axis 
    plt.xlabel('Perihelion date')
    plt.ylabel('Precession (arcsec)')
    
    plt.plot(numdate,arcsec,'bo')
    plt.xticks(numdate,strdate,rotation=45)
    
    slope = add2plot(numdate, arcsec)
    slope = round(slope * 365.25 * 100, 2)
    
    plt.title(f"Slope of best fit line: {slope} arcsec/cent")
    plt.savefig(f"{filename}.png", bbox_inches='tight')
    plt.show()



# Purpose: precesses data to extract relevant information for plotting
# Arguments: data (a list of dictionaries) containing dara to be precessed
# Side Effects: none
# Returns: a tuple of three lists (numdate, strdate, arcsec) that contain precessed data
def precess(data):
    numdate = []
    strdate = []
    arcsec = []
    v = np.array(data[0]['coord'])

    for datum in data:
        u = np.array(datum['coord'])
        ratio = np.dot(u, v) / np.sqrt(np.dot(u, u) * np.dot(v, v))

        if np.abs(ratio) <= 1:
            angle = 3600 * np.degrees(np.arccos(ratio))
            numdate.append(datum['numdate'])
            date = datum['strdate'].split(' ')[0]
            strdate.append(date)
            arcsec.append(angle)

    return (numdate, strdate, arcsec)



# Purpose: add a best-fit line to an existing plot based on linear regression
# Arguments: numdate (of type list) that contains a list of numerical dates
#            actual (of type list) that contains actual data points
# Side Effects: modifies an existing plot by adding a best-fit line and labels
# Returns: slope of the line of best fit
def add2plot(numdate,actual):
    r = stats.linregress(numdate,actual)
    bestfit = [r[0] * num + r[1] for num in numdate]
    plt.plot(numdate,bestfit,'b-')
    plt.legend(["Actual data","Best fit line"])
    
    # Return the slope of the line of best fit
    return r[0]
    

    
# Purpose: uses the argument 'data' to output a csv-file with the format implied by horizons_results_v2.csv
# Arguments: data (a list of dictionaries) that contains data to be saved
#            filename (of type string) that represents the name of the file to save the csv file as
# Side Effects: formats 'data' and creates a csv file with the proper format
# Returns: none
def savedata(data, filename):
    file = open(f"{filename}.csv", 'w')
    
    file.write("NUMDATE, STRDATE, XCOORD, YCOORD, ZCOORD\n") 
    for datum in data:
        num_date = '{:.6f}'.format(datum['numdate'])
        date = datum['strdate'].split(' ')[0]
        
        # format datum with 6 decimal points
        x_coordinate = '{:.6f}'.format(datum['coord'][0])
        y_coordinate = '{:.6f}'.format(datum['coord'][1])
        z_coordinate = '{:.6f}'.format(datum['coord'][2])
        
        # write formatted data to the csv-file
        file.write(f"{num_date}, {date}, {x_coordinate}, {y_coordinate}, {z_coordinate}\n")
            
    file.close()
    
   
    
# Purpose: refines data by reading files of format horizon_results_Year-Month-Day.txt and extracting perihelion data from them
# Arguments: data (a list of dictionaries) containing datum to be refined
#            filename (of type string) represents a file in txt form to load perihelion data from
# Side Effects: none
# Returns: refined_data (a list of dictionaries) containing the refined/improved data
def refine(data, filename):
    refined_data = []

    for datum in data:
        file_name = f"{filename}_{datum['strdate']}" 
        
        # Load data from said file
        file_data = loaddata(file_name)
        
        # Locate perihelia from said file
        perihelia = locate(file_data)

        if perihelia:
            # Add the first perihelion from said file to the list
            refined_data.append(perihelia[0])

    return refined_data



main()  