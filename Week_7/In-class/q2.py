def transform_string(input_str):
    string = ""
    num_upper = 0
    num_lower = 0
    num_digit = 0
    num_symbol = 0
    for ch in input_str:
        if ch.isdigit():
            num_digit += 1
            string += 'd'
        elif ch.isupper():
            num_upper += 1
            string += 'L'
        elif ch.islower():
            num_lower += 1
            string += 'l'
        else:
            num_symbol += 1
            string += 's'

    print("Number of uppercase letters", num_upper)
    print("Number of lowercase letters ", num_lower)
    print("Number of digits: ", num_digit)
    print("Number of symbols", num_symbol)
    return string

print(transform_string("IS1704 is a fun module"))
print("LLddddsllslslllsllllll")