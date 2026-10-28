def file_to_dict(file_name):
    mapping = {}

    with open(file_name, 'r') as file:
        for line in file:
            fields = line.strip().split("\t")
            id = ""
            for field in fields:
                field_variable, field_value = field.split(":")
                if field_variable == "ID" and field_value not in mapping:
                    mapping[field_value] = {}
                    id = field_value
                else:
                    mapping[id][field_variable] = field_value
    return mapping

employees = file_to_dict("employees.txt")

loop_bool = "Y"

while loop_bool != "N":
    employee_id_search = input("Enter an employee ID: ")
    if employee_id_search not in employees:
        print("Not found!")
    else:
        print(f"This employee is {employees[employee_id_search]["name"]}")
        field_search = input("\tEnter a field name or 'S' to stop: ")
        while field_search != "S":
            if field_search not in employees[employee_id_search]:
                print("\tNot found!")
            else: 
                print(f"\tThe {field_search} is {employees[employee_id_search][field_search]}.")
            
            field_search = input("\tEnter a field name or 'S' to stop: ")

    loop_bool = input("\nDo you want to search for another employee? [Y|N]:")
print("\nGood-bye!")