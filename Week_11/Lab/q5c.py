from q5a import count_words_in_file

word_mapping = count_words_in_file('spam_sms.txt')

most_frequent_10 = []
frequent_index_list = []

for word in word_mapping:
    frequency = word_mapping[word]
    if len(most_frequent_10) < 10:
        most_frequent_10.append((word, frequency))
        frequent_index_list.append(frequency)
    else:
        if frequency > min(frequent_index_list):
            index = frequent_index_list.index(min(frequent_index_list))
            most_frequent_10.pop(index)
            most_frequent_10.insert(index, (word, frequency))
            frequent_index_list.pop(index)
            frequent_index_list.insert(index, frequency)

# Sort 
for i in range(len(most_frequent_10)):
    for j in range(0, len(most_frequent_10) - i -1):
        if most_frequent_10[j][1] < most_frequent_10[j + 1][1]:
            temp = most_frequent_10[j]
            most_frequent_10[j] = most_frequent_10[j + 1]
            most_frequent_10[j + 1] = temp

print(most_frequent_10)