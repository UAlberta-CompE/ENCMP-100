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
# numbers, adding to 100%, follow-up questions may be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import numpy as np

print('Version 2')
# ----------Students write/modify their code below here ---------------------

# Prompts the user to enter a code
code = input('Please enter a code to break: ')
# Creates an array by separating each number in the code 
code = np.array(list(code),dtype=int)

# Define a list for rescue days
Rescue_Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Define a list for rendezvous points
Rendezvous_Point = ["bridge", "library", "river crossing", "airport", "bus terminal", "hospital", "railway station"]

# Proceeds only if code is a nine-digit number
if len(code) == 9:
    # Proceeds only if sum of code is odd
    if (sum(code) % 2) != 0:
        # calculate the deciphered 'day' and store it in a variable, then print it
        day = (code[2] * code[1]) - code[0]
        # Proceeds if numerical value of day is between 0 and 8 exclusive
        if 0 < day < 8:
            # Proceeds if 3rd digit of code raised to the power of 2nd digit is divisble by 3
            if (code[2] ** code[1]) % 3 == 0:
                # calculate the deciphered 'point' and store it in a variable
                point = code[5] - code[4]
            else:
                point = code[4] - code[5]
            # Proceeds if numerical value of point is between 0 and 8 exclusive
            if 0 < point < 8:
                # Outputs a message stating the success of the mission
                print("Rescued on " + Rescue_Day[day - 1] + " at the " + Rendezvous_Point[point - 1] + ".")
            else:
                print("Decoy Message: Invalid rendezvous point.")
        else:
            print("Decoy Message: Invalid rescue day.")
    else:
        print("Decoy Message: Sum is even.")
else:
    print("Decoy Message: Not a nine-digit number.")