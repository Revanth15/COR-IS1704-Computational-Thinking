# Name:
# Email ID:
#60m remaining
# 46
def load_pokedex(filename):
    # Replace the code below with your implementation.
    pokedex = []
    with open(filename, 'r') as p_file:
        headers = []
        counter = 1
        for entry in p_file:
            details = entry.strip().split(",")
            if counter == 1:
                headers = details 
            else:
                pokemon_entry = {}
                for i in range(len(headers)):
                    detail = details[i]
                    if detail == "":
                        detail = None
                    elif "." in detail:
                        detail = float(detail)
                    else:
                        digit_bool = True
                        for ch in detail:
                            if not ch.isdigit():
                                digit_bool = False

                        if digit_bool:
                            detail = int(detail)

                    pokemon_entry[headers[i]] = detail
                pokedex.append(pokemon_entry)
            counter += 1
    return pokedex
