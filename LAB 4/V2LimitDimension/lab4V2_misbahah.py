## TSPANALYZE  Geomatics and the Travelling Sales[person] Problem
#
# According to the ISO/TC 211, geomatics is the "discipline concerned
# with the collection, distribution, storage, analysis, processing, [and]
# presentation of geographic data or geographic information." Geomatics
# is associated with the travelling salesman problem (TSP), a fundamental
# computing problem. In this lab assignment, a University of Alberta
# student completes a Python program to analyze, process, and present
# entries, stored in a binary data file, of the TSPLIB, a database
# collected and distributed by the University of Heidelberg.
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
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt



# Defining main function that invokes the functions menu, tspPrint, and tspPlot and repeats itself until user inputs choice as 0
def main():
    tsp = io.loadmat('tspData.mat',squeeze_me=True)
    tsp = np.ndarray.tolist(tsp['tsp'])
    file = open('tspAbout.txt','r')
    print(file.read())
    file.close()
    
    choice = menu()
    
    while choice != 0:
        if choice == 1:
            tspPrint(tsp)
        
        elif choice == 2:
            tspLimit(tsp)
        
        elif choice == 3:
            tspPlot(tsp)
            
        choice = menu()



# Defining menu function that requires an input from user after giving 4 choices, and returns the choice
def menu():
    print()
    print("MAIN MENU")
    print("0. Exit program")
    print("1. Print database")
    print("2. Limit dimension")
    print("3. Plot one tour")
    print()
    
    choice = int(input("Choice (0-3)? "))
    
    while not (0 <= choice <= 3):
        choice = int(input("Choice (0-3)? "))
    
    return choice



# Defining tspPrint function that is invoked in main function when user input is 1
def tspPrint(tsp):
    print()
    print("NUM  FILE NAME  EDGE TYPE  DIMENSION  COMMENT")
    
    for k in range(1,len(tsp)):
        name = tsp[k][0]
        edge = tsp[k][5]
        dimension = tsp[k][3]
        comment = tsp[k][2]
        print("%3d  %-9.9s  %-9.9s  %9d  %s" % (k,name,edge,dimension,comment))



# Defining tspPlot function that is invoked in main function when user input is 3       
def tspPlot(tsp):
    num = int(input("Number (EUC_2D)? "))
    
    min_num = 1
    max_num = len(tsp) - 1
    while num < min_num or num > max_num:
        num = int(input("Number (EUC_2D)? "))
    
    edge = tsp[num][5]
    tsp1 = tsp[num]
    
    if edge == 'EUC_2D':
        print("See tspPlot.png")
        plotEuc2D(tsp1[10], tsp1[2], tsp1[0])
    else:
        print("Invalid (%s)!!!" % edge)
        
        

# Defining tspLimit function that computes and prints the max and min no. of cities, prompts user for input of a limit, and removes
# any record in tsp with a dimension greater than the limit inputted by the user
def tspLimit(tsp):
    
    # Creating a list to store all the dimensions (or no. of cities) in an array called dimensions
    dimensions = [dimension[3] for dimension in tsp[1:]]
    
    # Computing and storing the minimum and maximum value of all the data stored in dimensions array
    min_dimension = min(dimensions)
    max_dimension = max(dimensions)
    
    print("Min dimension:", min_dimension)
    print("Max dimension:", max_dimension)
    
    limit = int(input("Limit value? "))
    
    while not (min_dimension <= limit <= max_dimension):
        limit = int(input("Limit value? "))
        
    index = 1
    while index < len(tsp):
        if tsp[index][3] > limit:
            del tsp[index]
        else:
            index += 1
    
    return tsp
        


# Defining plotEuc2D fuction that is invoked in tspPlot function and the user inputs a valid EUC_2D number
# Plots a graph of the second column of the coord argument on the Y-axis, against the first column on the X-axis 
def plotEuc2D(coord, comment, name):
    
    plt.plot(coord[:, 0], coord[:, 1], 'o-',markersize = 4, linewidth = 1, label = name)
    plt.plot([coord[0, 0], coord[-1, 0]], [coord[0, 1], coord[-1, 1]], 'r-')
    plt.plot()
    
    plt.title(comment)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.legend(loc="upper right")
    
    plt.savefig('tspPlot.png')
    
    plt.show()


    
# Invoking the main function
main()
