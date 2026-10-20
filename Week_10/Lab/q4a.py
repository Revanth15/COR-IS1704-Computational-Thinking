with open("transactions.txt", "r") as transactions_list:
    with open("transactions-output-1.txt", "w") as output_file:
        for transaction in transactions_list:
            date, description, price = transaction.strip().split("\t")
            if float(price.strip("$")) >= 30: 
                output_file.write(f"{date}\t{description}\t{price}\n")
