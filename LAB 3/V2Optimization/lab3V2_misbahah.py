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
import matplotlib.pyplot as plt
import numpy as np

print('Version 1 - Solution')
# ------------Students edit/write their code below here--------------------------
# ------------Remove any code that is unnecessary--------------------------

# Assigning values to constants to be used throughout the program
MONTHLY_CONTRIBUTION = 200 # $
ANNUAL_INTEREST_RATE = 6.25 # % 
ANNUAL_TUITION_INCREASE = 7 # % 
YEARS = 18 # number of years
MONTHS = 12 # number of months

# Calculating monthly interest rate 
monthly_interest_rate = (ANNUAL_INTEREST_RATE / 100) / 12 

# Creating an array to store savings at the end of each month
monthly_savings = []
# Creating an array to store savings at the end of each year 
year_end_savings = []

# Creating variables to be used and aletered throughout the program
OLD_BALANCE = 2000 # $
NEW_BALANCE = OLD_BALANCE # $ 

# Creating an array to store tuition fee for Arts, Science, and Engineering respectively IN THAT ORDER
costs = [5550, 6150, 6550]
# Creating an array to add up the last 4 years of tuition fee for Arts, Science, and Engineering respectively IN THAT ORDER
total_tuition_fee = [0, 0, 0]



# Saving Calculation
# Calculate and store monthly balance of RESP account for the next (12 * 18) months
for year in range(0, YEARS + 1):
    year_end_savings = year_end_savings + [NEW_BALANCE]
    for month in range(1, MONTHS + 1): 
        if month == 1 and year == 0:
            pass
        else:
            NEW_BALANCE = OLD_BALANCE + (OLD_BALANCE * monthly_interest_rate) + MONTHLY_CONTRIBUTION
            OLD_BALANCE = NEW_BALANCE
        monthly_savings = monthly_savings + [NEW_BALANCE]
    


# Tuition Calculation
# Calculate and store the increase in tuition fee for the next 22 years
for year in range(YEARS + 4):
    for program in range(len(costs)):
        
        # Calculate tuition fee for the last 4 years
        if year > (YEARS - 1):
            total_tuition_fee[program] = total_tuition_fee[program] + costs[program]
            
        costs[program] = costs[program] + (costs[program] * (ANNUAL_TUITION_INCREASE / 100))



# Plot 
# storing x and y values
x_value = np.arange(0, MONTHS + YEARS * MONTHS)
y1_value = np.repeat(total_tuition_fee[0], 228)
y2_value = np.repeat(total_tuition_fee[1], 228)
y3_value = np.repeat(total_tuition_fee[2], 228)

# plotting all 4 graphs
plt.plot(x_value / 12, monthly_savings, label = "Saving Balance")
plt.plot(x_value / 12, y1_value, color='orange', label="Arts")
plt.plot(x_value / 12, y2_value, color='green', label="Science")
plt.plot(x_value / 12, y3_value, color='brown', label="Engineering")

# labelling and seting the limit for the axis
plt.title("Savings vs Tuition")
plt.xlabel("Years")
plt.ylabel("Amount $")
plt.xticks(np.arange(0, 19))
plt.xlim(0, 18)
plt.ylim(0, 100000)
plt.legend()
    


# Output
print("The savings amount is :", np.round(year_end_savings[-1], 2))
print("The cost of the arts program is :", np.round(total_tuition_fee[0], 2))
print("The cost of the science program is :", np.round(total_tuition_fee[1], 2))
print("The cost of the engg program is :", np.round(total_tuition_fee[2], 2))
plt.show()



#-----------------------------"""Version 2 starts from here"""-----------------------------
print('Version 2 - Solution')



# Optimization

#Get valid user input for program selection
valid = False
while valid == False:
    user_input = int(input("(1) Arts, (2) Science, (3) Engineering. Enter a number for the corresponding program : "))
    if user_input == 1 or user_input == 2 or user_input == 3:
        valid = True
    else:
        print("Invalid input.")


# Assign name of program inputted by user to a variable and asssign program cost for that program to a variable
program_name = ''
program_cost = 0
if user_input == 1:
    program_name = "Arts"
    program_cost = total_tuition_fee[0]
elif user_input == 2:
    program_name = "Science"
    program_cost = total_tuition_fee[1]
else:
    program_name = "Engineering"
    program_cost = total_tuition_fee[2]


# Output suitable message depending on savings vs cost of tuition
if year_end_savings[-1] >= program_cost:
    print("Congratulations!!! You have saved enough for the", program_name, " program.")
else:
    print("Unfortunately!!! You do not have enough saved for the", program_name, " program")


# Calculate optimal monthly contribution amount and output suitable message
SAVING_CALCULATOR = 2000
NEW_MONTHLY_CONTRIBUTION = 1

while SAVING_CALCULATOR < program_cost:
    SAVING_CALCULATOR = 2000
    NEW_MONTHLY_CONTRIBUTION = NEW_MONTHLY_CONTRIBUTION + 1
    for month in range((MONTHS * YEARS) -1):
        SAVING_CALCULATOR = SAVING_CALCULATOR + (SAVING_CALCULATOR * monthly_interest_rate + NEW_MONTHLY_CONTRIBUTION)

print("The optimal monthly contribution amount is $", np.round(NEW_MONTHLY_CONTRIBUTION))