with open("transactions.txt", "r") as transactions_list:
    with open("transactions-output-2.txt", "w") as output_file:
        month_name_list = []
        monthly_list = []
        for transaction in transactions_list:
            date, description, price = transaction.strip().split("\t")
            month_stripped = date[3:]
            if month_stripped not in month_name_list:
                month_name_list.append(month_stripped)
                monthly_list.append([(description, float(price.strip("$")))])
            else:
                index = month_name_list.index(month_stripped)
                monthly_list[index].append((description, float(price.strip("$"))))

        for i in range(len(month_name_list)):
            total = 0
            for transaction in monthly_list[i]:
                total += transaction[1]
            print(f"{month_name_list[i]}: total transaction amount if ${total}")
            for transaction in monthly_list[i]:
                print(f"\t{transaction[0]}\t${transaction[1]}")
            print()