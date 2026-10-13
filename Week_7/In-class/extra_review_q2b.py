def print_diamond_using_str(text):
    size_of_diamond = (len(text) - 2) / 2
    print(size_of_diamond)
    return size_of_diamond


print("Testcase 1: print_diamond_using_str('12345678')")
print('-' * 10)
print('Expected:')
print('   1')
print('  2 8')
print(' 3   7')
print('  4 6')
print('   5')
print('Actual:')
print_diamond_using_str('12345678')

print("\nTestcase 2: print_diamond_using_str('opqrstuvwxyz')")
print('-' * 10)
print('Expected:')
print('   o')
print('  p z')
print(' q   y')
print('r     x')
print(' s   w')
print('  t v')
print('   u')
print('Actual:')
print_diamond_using_str('opqrstuvwxyz')
