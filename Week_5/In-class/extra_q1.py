def reverse_words(sentence):
    reversed_string = ""
    for word in sentence.split(" "):
        reversed_string += word[::-1] + " "
    return reversed_string

print(reverse_words("I study at SMU"))
print(reverse_words("Python is a programming language."))