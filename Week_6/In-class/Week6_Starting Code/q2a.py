# Name: Revanth
# Email ID: revanth.rs.2026

def get_unique_titles(books_list):
    # Replace the code below with your implementation.
    unique_list = []
    for book in books_list:
        if book[0] not in unique_list:
            unique_list.append(book[0])
    return unique_list