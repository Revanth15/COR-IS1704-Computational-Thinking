def encode_message(text):
    pass


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
