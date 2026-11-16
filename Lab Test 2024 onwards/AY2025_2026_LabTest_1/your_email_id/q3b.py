# Name:
# Email ID:

def get_pokemon_info(pokemon_cards):  
    # Modify the code below.
    total_hp = 0
    strongest_attacker = ("def", -99999)
    strongest_defender = ("def", -99999)
    for card in pokemon_cards:
        name, category, hp, attack, defence = card
        total_hp += hp
        if attack > strongest_attacker[1]:
            strongest_attacker = (name, attack)
        if defence > strongest_defender[1]:
            strongest_defender = (name, defence)
    return (round(total_hp/len(pokemon_cards),2), strongest_attacker[0], strongest_defender[0])




