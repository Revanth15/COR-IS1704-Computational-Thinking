# Name:
# Email ID:
from q3a import get_counts
def get_best_avg(pokemon_cards, metric):
    # Modify the code below.
    category_index = ["electric", "fighting", "fire", "ground", "normal", "water"]
    pokemon_count = get_counts(pokemon_cards)
    total_metric = [0,0,0,0,0,0]
    average = [0,0,0,0,0,0]
    for card in pokemon_cards:
        name, category, hp, attack, defense = card
        category_idx = category_index.index(category)
        if category_idx != -1:
            if metric == 'hp':
                total_metric[category_idx] += hp
            elif metric == 'attack':
                total_metric[category_idx] += attack
            elif metric == 'defense':
                total_metric[category_idx] += defense
    for i in range(len(category_index)):
        average[i] = round(total_metric[i] / pokemon_count[i],2)

    max_stat = max(average)
    idx = average.index(max_stat)
    return (category_index[idx], max_stat)