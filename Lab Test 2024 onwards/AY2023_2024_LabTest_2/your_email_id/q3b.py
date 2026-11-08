# Name:
# Email ID:

# 46
# 37
def select_fields(pokedex, query):    
    # Replace the code below with your implementation.

    query_split = query.strip().split(" ")
        
    if len(query_split) == 1 and "select" in query_split:
        return pokedex
    
    if query_split != [] and "select" in query_split:
        index = query_split.index("select")
        query_split.pop(index)

    return_list = []
    for pokemon in pokedex:
        return_pokemon = {}
        for detail_heder in query_split:
            if detail_heder in pokemon.keys():
                return_pokemon[detail_heder] = pokemon[detail_heder]
        return_list.append(return_pokemon)

    return return_list
