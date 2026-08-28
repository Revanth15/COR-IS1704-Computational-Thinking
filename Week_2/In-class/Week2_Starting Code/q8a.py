# ################################################################################
# This function is for you to implement!
def calculate_tax_1(income):
    """
    This function assumes that the income is between $20,000 and $30,000.
    """
    
    # Modify the code below to return the right amount of tax.
    above_20k = income // 20000
    above_20k_tax_rate = (income - (above_20k * 20000)) * 2/100
    
    return above_20k_tax_rate
    
    
# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_1(25000.0))
