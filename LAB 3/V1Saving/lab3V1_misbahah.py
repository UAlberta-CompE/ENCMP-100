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

print('Version 1')
# ------------Students edit/write their code below here--------------------------
# ------------Remove any code that is unnecessary--------------------------

# Assigning values to constants
OLD_BALANCE = 2000
MONTHLY_CONTRIBUTION = 200
ANNUAL_INCREASE_RATE = 6.25
YEARS = 18
MONTHS = 12
TUITION_INCREASE_RATE = 7

monthly_interest_rate = (ANNUAL_INCREASE_RATE / 100) / 12
yearly_range = np.arange(0, YEARS + 1)
monthly_range = np.arange(0, MONTHS + YEARS * MONTHS)

# Creating empty arrays to append later and assinging old balance to a variable
amount = []
monthly_amount = []
NEW_BALANCE = OLD_BALANCE

for year in range(0, YEARS + 1):
    amount = amount + [np.round(NEW_BALANCE, 2)]
    for month in range(1, MONTHS + 1):
        if month == 1 and year == 0:
            pass
        else:
            NEW_BALANCE = OLD_BALANCE * (1 + monthly_interest_rate) + MONTHLY_CONTRIBUTION
            OLD_BALANCE = NEW_BALANCE
        monthly_amount = monthly_amount + [np.round(NEW_BALANCE, 2)]
        
costs = {'Art': 5550, 'Science': 6150, 'Engineering': 6550}
total_costs = {program: 0 for program in costs}

for year in range(1, 23):
    for program in costs:
        costs[program] = costs[program] * (1 + (TUITION_INCREASE_RATE / 100))
        if year in range(18, 22):
            total_costs[program] = total_costs[program] + costs[program]
            
#Code for plots
plt.plot(monthly_range/12, monthly_amount, label = 'Saving Balance')
plt.title('Savings vs Tuition')
plt.xlabel('Years')
plt.ylabel('Amount $')
print(f'The savings amount is ${amount[-1]}')

for program, total_cost in total_costs.items():
    print(f'The cost of the {program} program is ${round(total_cost, 2)}')
    color = {'Art': 'orange', 'Science': 'green', 'Engineering': 'brown'}[program]
    plt.axhline(total_cost, label=program, color=color)
plt.xticks(np.arange(0, 19))
plt.xlim(0, 18)
plt.ylim(0, 100000)
plt.legend()
plt.show()
