## Q3 PART 1
# This function is for you to implement!
def calculate_salary(monthly_sales):
    
    # This variable is defined for you to use.
    BASE_SALARY = 2000.0
    
    # ################################################################################
    # Modify the code below to return the right amount of salary.
    commision_rate = 5
    if 10000 <= monthly_sales < 15000:
        commision_rate = 10
    elif 15000 <= monthly_sales < 18000:
        commision_rate = 15
    elif monthly_sales >= 18000:
        commision_rate = 18

    salary = 2000 + (monthly_sales * (commision_rate/100))
    return salary
    # ################################################################################

## Q3 PART 2
# Write your code below

sales = int(input("Enter monthly sales amount($): "))
salary = calculate_salary(sales)
print(f"This monthly pay for the salesperson is ${salary}")