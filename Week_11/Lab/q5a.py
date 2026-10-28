## Q5a Word Counts
# write your code below

def count_words_in_file(file_name):
    word_mapping = {}

    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() not in word_mapping:
                    word_mapping[word.lower()] = 1
                else:
                    word_mapping[word.lower()] += 1

    return word_mapping