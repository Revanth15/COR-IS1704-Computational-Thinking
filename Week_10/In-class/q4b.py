search_bool = input("Do you want to search our news database? [Y|N] :")

while search_bool != "N":
    search_text = input("Enter a keyword or a keyphrase: ").lower()
    with open("news.txt", "r") as news_list:
        news_filtered_list = []
        for news in news_list:
            if search_text in news.lower():
                news_filtered_list.append(news)

    if news_filtered_list == []:
        print("\nThere are no matching headline!")
    else: 
        print(f"\nThere are {len(news_filtered_list)} matching headlines:")
        for i in range(len(news_filtered_list)):
            print(f"\t{str(i+1)}. {news_filtered_list[i]}", end="")
    search_bool = input("\nDo you want to search again? [Y|N] :")

print("Good-bye!")