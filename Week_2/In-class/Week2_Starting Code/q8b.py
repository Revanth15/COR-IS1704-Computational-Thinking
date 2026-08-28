# ################################################################################
# This function is for you to implement!
def calculate_tax_2(income):
    """
    This function assumes that the income is between $0 and $30,000.
    """
    
    # Modify the code below to return the right amount of tax.
    
    taxable_income = max(0, income - 20000)
    tax = taxable_income * 2/100

    return tax


# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_2(25000.0))
print(calculate_tax_2(10000.0))