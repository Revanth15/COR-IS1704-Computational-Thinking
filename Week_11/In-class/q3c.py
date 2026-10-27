def reverse_dict(dict):
    return_dict = {}

    for key in dict:
        return_dict[dict[key]] = key
    return return_dict


dictionary = {'Monday': 'swimming', 'Tuesday': 'basketball', 'Wednesday': 'tennis','Thursday': 'yoga', 'Friday': 'gymnastics'}

# print(reverse_dict(dictionary))