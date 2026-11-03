
word_map = {}
word_list = []
entered_string = input("Enter a string > ")
word_list.append(entered_string)

# Gather the words
while entered_string != "":
    entered_string = input("Enter a string > ")
    if entered_string != "":
        word_list.append(entered_string)

# Count the first characters
for word in word_list:
    first_character = word[0].lower()
    if first_character not in word_map:
        word_map[first_character] = 1
    else:
        word_map[first_character] += 1

# Display it
for item in word_map:
    if item.isalpha():
        print(f"{word_map[item]} string{'s' if word_map[item] > 1 else ''} starting with '{item.upper()}' or '{item.lower()}'")
    else:
        print(f"{word_map[item]} string{'s' if word_map[item] > 1 else ''} starting with '{item}'")
