# Name:
# Email ID:

# 6m
def generate_loan_report(filename, bank_code):
    # Replace the code below with your implementation.
    return_list = []
    total_amount = 0
    with open(filename, 'r') as loan_file:
        for line in loan_file:
            nric, branch_id, loan_type, amount = line.strip().split(",")

            if bank_code in branch_id:
                return_list.append((nric,branch_id,loan_type,int(amount.strip("$"))))
                total_amount += int(amount.strip("$"))
        if len(return_list) != 0:
            return_list.append(('Total Loan Amount', total_amount))
    return  return_list
        
        

