def crack_pin(pin):
    pass


print('Testcase 1')
print('-' * 10)
print("Expected: '007'")
pin = '007'
result = crack_pin(pin)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: '0'")
pin = '0'
result = crack_pin(pin)
print('Actual:   ' + str(result))
