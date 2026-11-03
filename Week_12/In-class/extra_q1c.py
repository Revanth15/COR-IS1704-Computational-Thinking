import datetime

date_elements = str(datetime.date.today()).split("-")
current_month = int(date_elements[1])
current_day = int(date_elements[2])


no_of_days_in_month = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

continue_adding_task = input("Do you want to enter a task? [Y|N] :")

task_dict = {}

while continue_adding_task != "N":
    task_description = input("\nEnter task description:")

    month_valid = False
    while not month_valid:
        task_month = input("Enter the month it is due:").strip()
        if task_month.isdigit() and 1 <= int(task_month) <= 12:
            if current_month <= int(task_month):
                month_valid = True
                task_month = int(task_month)
            else:
                print("Sorry, the month has passed.\n")
        else:
            print("Sorry, invalid month!\n")

    date_valid = False
    while not date_valid:
        task_date = input("Enter the date it is due:").strip()
        if task_date.isdigit() and 1 <= int(task_date) <= no_of_days_in_month[int(task_month)]:
            if current_day <= int(task_date):
                date_valid = True
                task_date = int(task_date)
            else:
                print("Sorry, the date has passed.\n")
        else:
            print("Sorry, invalid date!\n")

    if task_month not in task_dict:
        task_dict[task_month] = {}
    if task_date not in task_dict[task_month]:
        task_dict[task_month][task_date] = []
    task_dict[task_month][task_date].append(task_description)

    print(f"\n{task_description} due on {task_date}/{task_month} has been recorded.")

    continue_adding_task = input("\nDo you want to continue? [Y|N] :")

print("\nHere are the tasks you've entered:")

sorted_month_list = sorted(task_dict.keys())
for month in sorted_month_list:
    sorted_date_list = sorted(task_dict[month].keys())
    for date in sorted_date_list:
        print(f"\nDue on {date}/{month}:")
        for task in task_dict[month][date]:
            print(f"\t{task}")