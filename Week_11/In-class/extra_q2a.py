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

def degrees_of_freedom(x, n):
    friends = []
    friends_check = []

    if n >= 1:
        friends += graph[x]
        n -= 1

    while n > 0:
        if friends_check == []:
            friends_check = graph[x]
        else:
            friends_check = friends[:]

        for friend in friends_check:
            friends += graph[friend]
        n -= 1
    friends = list(set(friends))
    friends.sort()
    if x in friends:
        friends.remove(x)
    return friends

graph = read_to_dict('friends.txt')

print(degrees_of_freedom("E", 1))
print(degrees_of_freedom("E", 2))
print(degrees_of_freedom("E", 3))