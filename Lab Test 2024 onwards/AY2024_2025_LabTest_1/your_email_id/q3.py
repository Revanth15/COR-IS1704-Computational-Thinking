# Name:
# Email ID:

def process_patient_data(patients):
    # Replace the code below with your implementation.
    return_values = [0, 0, 0, []]
    total_age = 0
    for patient in patients:
        name, age, gender, ailments, discharged = patient
        if gender == 'Male':
            return_values[0] += 1
        elif gender == 'Female':
            return_values[1] += 1
        
        if discharged:
            return_values[2] += 1

        total_age += age

        return_values[3] += ailments
    return (round(total_age/len(patients),2), return_values[0], return_values[1], return_values[2], list(set(return_values[3])))

    
