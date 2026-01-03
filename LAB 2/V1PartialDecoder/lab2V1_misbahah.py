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

print('Version 1')
# ----------Students write/modify their code below here ---------------------

# Prompts the user to enter a code
code = input('Please enter a code to break: ')
# Creates an array by separating each number in the code 
code = np.array(list(code),dtype=int)

# Proceeds only if code is a nine-digit number
if len(code) == 9:
    # Proceeds only if sum of code is odd
    if (sum(code) % 2) != 0:
        # calculate the deciphered 'day' and store it in a variable, then print it
        day = (code[2] * code[1]) - code[0]
        print("Day = ", day)
        # Proceeds if 3rd digit of code raised to the power of 2nd digit is divisble by 3
        if (code[2] ** code[1]) % 3 == 0:
            # calculate the deciphered 'place' and store it in a variable
            place = code[5] - code[4]
        else:
            place = code[4] - code[5]
        # Outputs deciphered 'place'
        print("Place = ", place)
    else:
        # Outputs sum of code is even
        print("Decoy Message: Sum is even.")
else:
    # Outputs code is not a nine-digit number
    print("Decoy Message: Not a nine-digit number.")