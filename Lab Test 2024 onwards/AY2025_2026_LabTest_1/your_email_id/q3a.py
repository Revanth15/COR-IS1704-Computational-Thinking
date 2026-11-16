# Name:
# Email ID:
    
def get_counts(pokemon_cards):
    # Modify the code below.
    pokemon_category_count = [0,0,0,0,0,0]
    for card in pokemon_cards:
        name, category, hp, attack, defence = card
        if category == "electric":
            pokemon_category_count[0] += 1
        elif category == "fighting":
            pokemon_category_count[1] += 1
        elif category == "fire":
            pokemon_category_count[2] += 1
        elif category == "ground":
            pokemon_category_count[3] += 1
        elif category == "normal":
            pokemon_category_count[4] += 1
        elif category == "water":
            pokemon_category_count[5] += 1
    return tuple(pokemon_category_count)





