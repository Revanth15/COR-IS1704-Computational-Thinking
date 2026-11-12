def get_document_pair(filename):
    # Modify the code below.

    dict_map = {}
    with open(filename, 'r') as dfile:
        for line in dfile:
            idx, content = line.strip().split("\t")
            content_words = content.strip().split(" ")
            unique_words = list(set(content_words))
            dict_map[idx] = unique_words

    unique_pair_max = 0
    unique_pair = (0,0)
    for i in dict_map.keys():
        for j in dict_map.keys():
            if i != j:
                common_words = set(dict_map[i]).intersection(set(dict_map[j]))
                if len(common_words) > unique_pair_max:
                    unique_pair = (i,j)
                    unique_pair_max = len(common_words)

    return (unique_pair[0], unique_pair[1], unique_pair_max)

