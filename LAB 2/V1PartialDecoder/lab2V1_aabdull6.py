# Student name: Ali Abdullah
# Student CCID: aabdull6
# Others:
import numpy as np  
print('Version 1')
code = input('Please enter a code to break: ')
code = np.array(list(code), dtype=int)
code_sum = sum(code)
day = (code[2] * code[1]) - code[0]
power = code[2] ** code[1]
if len(code) == 9:
    if code_sum % 2 != 0:
        day = (code[2]*code[1]) - code[0]
        print('day =', day)
        if (power / 3).is_integer():
            place = (code[5] - code[4])
            print('place =', place)
        else:
            place = (code[4] - code[5])
            print('place =', place)
    else:        
        print('Decoy Message: Sum is even.')
else:
    print('Decoy Message: Not a nine-digit number.')




