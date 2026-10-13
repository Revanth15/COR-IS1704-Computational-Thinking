def print_diamond(n):
    halves = n - 1
    middle = halves + 1
    full_length = n * 2 - 1
    for i in range(0,full_length):
        gap = abs(halves-i)
        if i == 0 or i == full_length-1:
            print(" " * (halves) + "*")
        else:
            print(" " * abs(halves - i) + "*" + " " * (full_length - (gap * 2) - 2) + "*")
    # pass


"""
n = 4
halves = 3
middle = 4
full length = 7
   *        => 3 left, sign              | i = 0
  * *       => 2 left, sign, 1 mid, sign | i = 1
 *   *      => 1 left, sign, 3 mid, sign | i = 2
*     *     => 0 left, sign, 5 min, sign | i = 3
 *   *      => 1 left, sign, 3 mid, sign | i = 4
  * *       => 2 left, sign, 1 mid, sign | i = 5
   *        => 3 left, sign              | i = 0
"""

print('Testcase 1: print_diamond(4)')
print('-' * 10)
print('Expected:')
print('   *')
print('  * *')
print(' *   *')
print('*     *')
print(' *   *')
print('  * *')
print('   *')
print('Actual:')
print_diamond(4)

print('\nTestcase 2: print_diamond(2)')
print('-' * 10)
print('Expected:')
print(' *')
print('* *')
print(' *')
print('Actual:')
print_diamond(2)
