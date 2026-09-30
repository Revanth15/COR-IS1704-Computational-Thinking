def bubble_sort(lst):
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                curr = lst[j]
                next = lst[j+1]
                lst[j] = next
                lst[j+1] = curr
                swapped = True
        if not swapped:
            break

    return lst

# Complexity is O(n^n-1) 
# where n is the number of list items

print('Testcase 1')
print('-' * 10)
print('Expected: [11, 12, 22, 25, 34, 64, 90]')
my_list = [64, 34, 25, 12, 22, 11, 90]
result = bubble_sort(my_list)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print('Expected: [1, 2, 3, 4]')
my_list = [1, 2, 3, 4]
result = bubble_sort(my_list)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print('Expected: [1, 1, 2, 3]')
my_list = [3, 1, 2, 1]
result = bubble_sort(my_list)
print('Actual:   ' + str(result))


# Cleaner version:
"""
def bubble_sort(lst):
    for i in range(len(lst)):
        swapped = False

        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

    return lst
    
For each pass:
    swapped = False

    compare every adjacent pair
        if out of order:
            swap
            swapped = True

    after the WHOLE pass:
        if nothing was swapped:
            list is sorted → stop

    
"""