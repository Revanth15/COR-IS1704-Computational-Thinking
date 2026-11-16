# Name:
# Email ID:
from q2a import calculate_bmr
def find_people_in_range(people, bmr_range):
    # Modify the code below.
    bmr_min, bmr_max = bmr_range
    counter = 1
    return_str = ""
    for p in people:
        name, weight, height, age, gender = p
        bmr = calculate_bmr(weight,height,age,gender)
        if bmr_min <= bmr < bmr_max:
            if counter != 1:
                return_str += "-"
            return_str += f"{str(counter)}-{name}({bmr})"
            counter += 1
    return return_str

