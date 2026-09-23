# Name: Revanth
# Email ID: revanth.rs.2026


def get_titles_and_counts(books_list):
    # Replace the code below with your implementation.
    count = []
    titles = []
    final_list=[]
    for book in books_list:
        if book[0] not in titles:
            titles.append(book[0])
            count.append(book[3])
        else:
            index = titles.index(book[0])
            count[index] += book[3]

    for i in range(len(titles)):
        final_list.append((titles[i], count[i]))

    return final_list