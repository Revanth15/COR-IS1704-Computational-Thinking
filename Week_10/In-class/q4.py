
search_text = input("Enter a keyword or a keyphrase: ").lower()

with open("news.txt", "r") as news_list:
    counter = 1
    for news in news_list:
        if search_text in news.lower():
            print(f"{str(counter)}. {news}", end="")
            counter += 1