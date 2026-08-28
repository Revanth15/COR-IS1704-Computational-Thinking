#Lab2_Q4
# #####################################
# Write your code below to first define 
# the function calculate_interest()

def calculate_interest(principal, annual_interest_rate, frequency_of_compounding, deposit_period):
    total_interest = (principal * ((1 + ( annual_interest_rate / frequency_of_compounding)) ** (frequency_of_compounding * deposit_period))) - principal
    return round(total_interest, 2)

# ################################################################
# The default annual interest rate of 0.5%, compounded 
# monthly, has been provided for you.

# Annual interest rate (which is fixed)
ANNUAL_INTEREST_RATE = 0.005
# Number of times the interest is compounded per year
FREQUENCY_OF_COMPOUNDING = 12

# ################################################################
# Write your code below to prompt the user and display the 
# interest earned.

principal = float(input("What's the amount of your principal? "))
deposit_period = float(input("How many years do you want to deposit the money?"))
interest = calculate_interest(principal, ANNUAL_INTEREST_RATE, FREQUENCY_OF_COMPOUNDING, deposit_period)
print(f"The interest you will earn is ${interest}")


