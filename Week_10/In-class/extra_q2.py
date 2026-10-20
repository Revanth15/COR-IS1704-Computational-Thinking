with open("article-1.txt", "r") as article:
    word_list = []
    count_list = [] 
    for line in article:
        words = line.lower().split()
        for word in words:
            word = word.strip(".,!?;:\"()'")

            if word not in word_list:
                word_list.append(word)
                count_list.append(1)
            else:
                index = word_list.index(word)
                count_list[index] = count_list[index] + 1

    new_count_list = count_list[:]

    new_count_list.sort(reverse=True)
    for i in range(3):
        index = count_list.index(new_count_list[i])
        print(f"{word_list[index]}: {new_count_list[i]}")