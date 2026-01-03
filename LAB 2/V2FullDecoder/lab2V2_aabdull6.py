# Student name: Ali Abdullah
# Student CCID: aabdull6
# Others:
import numpy as np    
print('Version 2')
rescue_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
rendezvous_point = ['bridge', 'library', 'river crossing', 'airport', 'bus terminal', 'hospital', 'railway station']
code = input('Please enter a code to break: ')
code = np.array(list(code), dtype=int)
code_sum = sum(code)
day = (code[2] * code[1]) - code[0]
power = code[2] ** code[1]
if len(code) == 9:
    if code_sum % 2 != 0:
       if 0 < day <= 7:
           if (power / 3).is_integer():
                   place = (code[5] - code[4])  
           else:
                   place = (code[4] - code[5])
           if place >= 0 and place <= 7:
                       print('Rescued on', rescue_day[day-1], 'at the', rendezvous_point[place-1])
           else:
                       print('Decoy message: Invalid rendezvous point.')        
       else:
           print('Decoy message: Invalid rescue day.')
    else:        
        print('Decoy Message: Sum is even.')
else:
    print('Decoy Message: Not a nine-digit number.')
    
    
    
    
    
""" NOTE TO TA: Below is the same code with added annotations for your convenience. 
    Mark which ever one you prefer. If you do not have a preference, mark the unannotated code. 
    Thanks :)"""
    
    
                                    #Inital setup
# Import NumPy
import numpy as np    

# Print the version no.
print('Version 2')
# Define a list of days for rescue
rescue_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Define a list of rendezvous points
rendezvous_point = ['bridge', 'library', 'river crossing', 'airport', 'bus terminal', 'hospital', 'railway station']
# Prompt the user to enter a code for processing
code = input('Please enter a code to break: ')
# Convert the entered code into a NumPy array of integers
code = np.array(list(code), dtype=int)
                                    #Inital calculations required for determining validity of rules
# Calculate the sum of the digits in the code
code_sum = sum(code)
# Calculate 'day' based on 3rd element of code multiplying with the 2nd, subtracting the 1st element (Note: numbers shifted down 1 since arrays start from 0)
day = (code[2] * code[1]) - code[0]
# Calculate 'power' based on the third element of 'code' to the power of the 2nd element.
power = code[2] ** code[1]
                                    # Following is a series of nested if statements, which check the validity of rules 1,2,3,4 in order. 
                                    # If a rule is not satified, a corresponding error message is outputed and the if statements are exited.
                                    # Since there is no code after the loop, the program terminates/ends after the first rule failed.
# Check if the length of the entered code is 9
if len(code) == 9:
    # Check if the sum of the digits is odd
    if code_sum % 2 != 0:
        # Check if 'day' is within the valid range (1 to 7)
        if 0 < day <= 7:
            # Check if the result of power divided by 3 is an integer
            if (power / 3).is_integer():  #(NOTE: '% 3 =' could've also been used. I used ''is.integer'' for variety' )
                # Calculate 'place' based on the 6th - 5th or 5th -6th depending on if the power is divisible by 3 or not
                place = (code[5] - code[4])  
            else:
                # Calculate 'place' based on a different mathematical expression involving elements of 'code'
                place = (code[4] - code[5])
            
            # Check if 'place' is within a valid range (1 to 7)
            if place >= 0 and place <= 7:
                # Print the rescue information (Note: as before we have to shift the values since arrays start from 0)
                print('Rescued on', rescue_day[day-1], 'at the', rendezvous_point[place-1])
            else:
                # Print a message indicating an invalid rendezvous point
                print('Decoy message: Invalid rendezvous point.')        
        else:
            # Print a message indicating an invalid rescue day
            print('Decoy message: Invalid rescue day.')
    else:
        # Print a message indicating that the sum is even
        print('Decoy Message: Sum is even.')
else:
    # Print a message indicating that the entered code is not a nine-digit number
    print('Decoy Message: Not a nine-digit number.')
