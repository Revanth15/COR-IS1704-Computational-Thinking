def read_to_dict(file_name):
    graph = {}
    with open(file_name, 'r') as friends:
        for row in friends:
            a, b = row.strip().split("\t")
            if a in graph:
                if b not in graph[a]:
                    graph[a].append(b)
            else:
                graph[a] = [b]

            if b in graph:
                if a not in graph[b]:
                    graph[b].append(a)
            else:
                graph[b] = [a]

    return graph

def exact_degrees_of_freedom(x, n):
    friends = []
    friends_from_last = []
    friends_check = []

    if n >= 1:
        friends += graph[x]
        n -= 1

    while n > 0:
        if friends_check == []:
            friends_check = graph[x]
        else:
            friends_check = friends[:]
        if n == 1:
            friends_from_last = friends[:]
        for friend in friends_check:
            friends += graph[friend]
        n -= 1
    friends = set(friends)
    friends_from_last = set(friends_from_last)
    exact = list(friends.difference(friends_from_last))
    exact.sort()
    if x in exact:
        exact.remove(x)
    return exact

graph = read_to_dict('friends.txt')

# Test Cases for Q2(b): people exactly n degrees away from E
print("\nTest Case #1: E is 1 degree away")
print("Expected:")
print("['B']")
print("Actual  :")
print(exact_degrees_of_freedom("E", 1))

print("\n==========\n")

print("Test Case #2: E is 2 degrees away")
print("Expected:")
print("['A', 'C']")
print("Actual  :")
print(exact_degrees_of_freedom("E", 2))

print("\n==========\n")

print("Test Case #3: E is 3 degrees away")
print("Expected:")
print("['D', 'F']")
print("Actual  :")
print(exact_degrees_of_freedom("E", 3))

print("\n==========\n")

print("Test Case #4: E is 4 degrees away")
print("Expected:")
print("['G']")
print("Actual  :")
print(exact_degrees_of_freedom("E", 4))
