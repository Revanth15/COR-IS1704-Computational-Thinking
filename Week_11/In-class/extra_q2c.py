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

def degrees_of_separation(x, y):
    if x == y:
        return 0

    friends = []
    friends_check = []
    counter = 1
    friends += graph[x]

    while True:
        if y in friends:
            return counter
        
        if friends_check == []:
            friends_check = graph[x]
        else:
            friends_check = friends[:]

        for friend in friends_check:
            friends += graph[friend]
        counter += 1

graph = read_to_dict('friends.txt')

# Test Cases for Q2(c)
# Implement degrees_of_separation(name_1, name_2) to return the shortest distance.
print("\nTest Case #1: A to E")
print("Expected:")
print("2")
print("Actual  :")
print(degrees_of_separation("A", "E"))

print("\n==========\n")

print("Test Case #2: B to G")
print("Expected:")
print("3")
print("Actual  :")
print(degrees_of_separation("B", "G"))

print("\n==========\n")

print("Test Case #3: A to G")
print("Expected:")
print("2")
print("Actual  :")
print(degrees_of_separation("A", "G"))

print("\n==========\n")

print("Test Case #4: E to G")
print("Expected:")
print("4")
print("Actual  :")
print(degrees_of_separation("E", "G"))
