word = input("Enter a word :")

def is_palindrome(word):
    word_reversed = word[::-1]
    if word == word_reversed:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is NOT a palindrome.")

is_palindrome(word)