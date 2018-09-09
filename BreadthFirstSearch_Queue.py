

def bfs(graph, StartPoint):

    q = [StartPoint]
    path = []

    while q:

        current = q.pop()

        path.append(current)

        for i in graph[current]:
            if i not in q:
                q.insert(0,i)

    return path




adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(bfs(adjacency_matrix, 1))
