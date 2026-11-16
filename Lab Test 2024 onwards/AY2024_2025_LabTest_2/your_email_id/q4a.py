# Name:
# Email ID:

def get_invalid_transactions(filename):
    # Replace the code below with your implementation.
    
    accounts = {}
    invalid_trans = []
    with open(filename, 'r') as transactions:
        for line in transactions:
            elems = line.strip().split("|")
            txID = elems[0]
            elems.pop(0)

            print(elems)

            total_input = 0
            invalid_trans_bool = False
            for txn in elems:
                if not invalid_trans_bool:
                    method, user, amount = txn.split(":")
                    amount = int(amount)
                    if user not in accounts.keys():
                        accounts[user] = []

                    
                    if method == "IN":
                        total_input += amount
                        if user != "COINBASE":
                            total_avail = sum(accounts[user])
                            if total_avail < amount:
                                invalid_trans.append(txID)
                                invalid_trans_bool = True
                                continue
                    elif method == "OUT":
                        total_input -= amount
            
            if total_input != 0:
                invalid_trans.append(txID)
            else:
                for txn in elems:
                    method, user, amount = txn.split(":")
                    amount = int(amount)
                    
                    if method == "IN":
                        if user != "COINBASE":
                            indexes_to_pop = []
                            adjustment = 0
                            for i in range(len(accounts[user])):
                                print(i)
                                print(txID, accounts, user)
                                coin = accounts[user][i]
                                if amount < coin:
                                    change = coin - amount
                                    accounts[user].insert(0, change)
                                    adjustment += 1
                                    continue
                                else:
                                    amount -= coin
                            for index in indexes_to_pop:
                                accounts[user].pop(index + adjustment)
                                indexes_to_pop = max(0, indexes_to_pop - 1)
                    elif method == "OUT":
                        accounts[user].append(amount)
                
    print(accounts)
    return list(set(invalid_trans))

# def get_invalid_transactions(filename):
#     # Replace the code below with your implementation.
    
#     accounts = {}
#     invalid_trans = []
#     with open(filename, 'r') as transactions:
#         for line in transactions:
#             elems = line.strip().split("|")
#             txID = elems[0]
#             elems.pop(0)

#             print(elems)

#             total_input = 0
#             invalid_trans_bool = False
#             for txn in elems:
#                 if not invalid_trans_bool:
#                     method, user, amount = txn.split(":")
#                     amount = int(amount)
#                     if user not in accounts.keys():
#                         accounts[user] = []

                    
#                     if method == "IN":
#                         total_input += amount
#                         if user != "COINBASE":
#                             total_avail = sum(accounts[user])
#                             if total_avail < amount:
#                                 invalid_trans.append(txID)
#                                 invalid_trans_bool = True
#                                 continue
#                     elif method == "OUT":
#                         total_input -= amount
            
#             if total_input != 0:
#                 invalid_trans.append(txID)
#             else:
#                 for txn in elems:
#                     method, user, amount = txn.split(":")
#                     amount = int(amount)
                    
#                     if method == "IN":
#                         if user != "COINBASE":
#                             for i in range(len(accounts[user])):
#                                 print(i)
#                                 print(txID, accounts, user)
#                                 coin = accounts[user][i]
#                                 accounts[user].pop(i)
#                                 if amount < coin:
#                                     change = coin - amount
#                                     accounts[user].insert(change, 0)
#                                     continue
#                                 else:
#                                     amount -= coin
#                     elif method == "OUT":
#                         accounts[user].append(amount)
                
#     print(accounts)
#     return list(set(invalid_trans))