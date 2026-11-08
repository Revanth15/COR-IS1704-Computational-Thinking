# Name:
# Email ID:
#5m
def get_special_word_count(filename):
    # The line of code below is for you to use. DO NOT modify it.
    special_chars = ".,;:!?()[]{}-~&*/+-=%$#@^_'\"<>"
    
    # Replace the code below with your implementation.

    special_words_count = 0

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split(" ")
            for word in words:
                for ch in word:
                    if ch in special_chars:
                        special_words_count += 1
                        break
    
    return special_words_count
