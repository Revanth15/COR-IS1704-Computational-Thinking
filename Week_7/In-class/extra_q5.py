import getpass

def crack_pin(pin):
    length_of_password = len(pin)
    max_num = 10 ** length_of_password
    for i in range(max_num):
        adjusted_to_num_of_characters = f"{i:0{length_of_password}d}"
        if adjusted_to_num_of_characters == pin:
            return adjusted_to_num_of_characters


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

PIN = getpass.getpass()
print(crack_pin(PIN))

# Time complexity is O(n)