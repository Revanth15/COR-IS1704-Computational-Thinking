# ################################################################################
# This function is for you to implement!
def calculate_tax_3(income):
    """
    This function assumes that the income is between $0 and $40,000.
    """
    
    # Modify the code below to return the right amount of tax.
    taxable_income = max(0, income - 20000)
    tax_20k = min(200 , taxable_income * 2/100)

    taxable_income = max(0, income - 30000)
    tax_30k = taxable_income * 3.5/100

    return tax_20k + tax_30k



# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_3(25000.0)) # 100.0
print(calculate_tax_3(10000.0)) # 0.0
print(calculate_tax_3(35000.0)) # 375.0

# ################################################################################

def calculate_tax_all(income):
    tax_20k = max(0, 0 + (income - 20000) * 0.02)
    tax_30k = max(0, 200 + (income - 30000) * 0.035)
    tax_40k = max(0, 550 + (income - 40000) * 0.07)
    tax_80k = max(0, 3350 + (income - 80000) * 0.115)
    tax_120k = max(0, 7650 + (income - 120000) * 0.15)
    tax_160k = max(0, 13950 + (income - 160000) * 0.18)
    tax_200k = max(0, 21150 + (income - 200000) * 0.19)
    tax_240k = max(0, 28750 + (income - 240000) * 0.195)
    tax_280k = max(0, 36550 + (income - 280000) * 0.20)
    tax_320k = max(0, 44550 + (income - 320000) * 0.22)

    tax = max(tax_20k, tax_30k, tax_40k, tax_80k, tax_120k, tax_160k, tax_200k, tax_240k, tax_280k, tax_320k)
    return tax

print(calculate_tax_all(81040))