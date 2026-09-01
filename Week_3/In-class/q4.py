def calculate_income_tax(annual_taxable_income):
    if annual_taxable_income < 20000:
        return 0 
    elif annual_taxable_income <= 30000:
        return ((annual_taxable_income - 30000) * 0.02)
    elif annual_taxable_income <= 40000:
        return 200 + ((annual_taxable_income - 30000) * 0.035)
    elif annual_taxable_income <= 80000:
        return 550 + ((annual_taxable_income - 40000) * 0.07)
    elif annual_taxable_income <= 120000:
        return 3350 + ((annual_taxable_income - 80000) * 0.115)
    elif annual_taxable_income <= 160000:
        return 7950 + ((annual_taxable_income - 120000) * 0.15)
    elif annual_taxable_income <= 200000:
        return 13960 + ((annual_taxable_income - 160000) * 0.18)
    elif annual_taxable_income <= 240000:
        return 21150 + ((annual_taxable_income - 200000) * 0.19)
    elif annual_taxable_income <= 280000:
        return 28750 + ((annual_taxable_income - 240000) * 0.195)
    elif annual_taxable_income <= 320000:
        return 36550 + ((annual_taxable_income - 280000) * 0.20)
    else:
        return 44550 + ((annual_taxable_income - 320000) * 0.22)

annual_taxable_income = int(input("Enter your annual taxable income: "))
print(f"Your total tax is ${calculate_income_tax(annual_taxable_income)}")