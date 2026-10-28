from q5a import count_words_in_file

word_mapping = count_words_in_file('spam_sms.txt')

for word in word_mapping:
    if len(word) >= 4 and word_mapping[word] > 50:
        print(f"{word}\t:\t{word_mapping[word]}")