import random

def scramble_word(word):
    scrambled_word = []
    characters_to_add = word[-1]
    remaining_chars = word[1:-1]
    punctuation_to_remain = []
    if len(word) <= 3:
        return word
    scrambled_word.append(word[0])

    if word[-1] in ",.[]{}()/';:&!?":
        characters_to_add = word[-2:]
        remaining_chars = word[1:-2]

    for i in range(len(remaining_chars)):
        if not remaining_chars[i].isalnum():
            punctuation_index = list(remaining_chars).index(remaining_chars[i])
            punctuation_to_remain.append((punctuation_index + 1, remaining_chars[i]))
        else:
            random_index = random.randint(1,len(remaining_chars)-1)
            scrambled_word.insert(random_index, remaining_chars[i])

    for punc in punctuation_to_remain:
        scrambled_word.insert(punc[0], punc[1])

    scrambled_word.append(characters_to_add)
    return "".join(scrambled_word)

with open("talk.txt", 'r') as talk_file:
    for line in talk_file:
        words = line.strip().split() 
        for word in words:
            print(scramble_word(word), end=" ")