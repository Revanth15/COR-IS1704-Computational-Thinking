def encode_message(text):
    current_ch = ""
    ch_counter = 0
    return_str = ""
    if text == "":
        return text
    for ch in text:
        if current_ch == "":
            current_ch = ch

        if ch == current_ch:
            ch_counter += 1
        else:
            return_str += " " + current_ch + str(ch_counter)
            current_ch = ch
            ch_counter = 1

    return_str += " " + current_ch + str(ch_counter)

    return return_str


print('Testcase 1')
print('-' * 10)
print("Expected: 'a3 b2 c5 d1 e1'")
text = 'aaabbcccccde'
result = encode_message(text)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: '12 21 33 &2 $1 910'")
text = '112333&&$9999999999'
result = encode_message(text)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print("Expected: ''")
text = ''
result = encode_message(text)
print('Actual:   ' + str(result))
