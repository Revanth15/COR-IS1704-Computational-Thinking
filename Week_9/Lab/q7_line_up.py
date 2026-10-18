# Q7: [★★★] Line-up

def get_lineup(info):
    lineup = []
    last_index = 0
    if info == []:
        return lineup
    for item in info:
        if "" in item:
            last_index = info.index(item)
            lineup.append(item[0])
    while True:
        updated_bool = False
        for item in info:
            if item[1] == lineup[0]:
                lineup.insert(0, item[0])
                updated_bool = True

        if not updated_bool: 
            break
    return lineup

print('Testcase 1')
print('-' * 10)
print("Expected: ['Alice', 'Bob', 'Chris', 'Darren']")
info = [('Chris', 'Darren'), ('Alice', 'Bob'), ('Darren', ''),
        ('Bob', 'Chris')]
result = get_lineup(info)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: ['John', 'Alan', 'Christie', 'Mary', 'Jason', 'George']")
info = [('Mary', 'Jason'), ('John', 'Alan'), ('Jason', 'George'),
        ('Alan', 'Christie'), ('Christie', 'Mary'), ('George', '')]
result = get_lineup(info)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print('Expected: []')
info = []
result = get_lineup(info)
print('Actual:   ' + str(result))
