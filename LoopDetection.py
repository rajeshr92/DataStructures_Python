

def LoopBFS(graph, StartPoint):

    q = [StartPoint]
    path = []

    while q:

        current = q.pop()

        path.append(current)

        for i in graph[current]:
            if i in path:
                return True
            elif i not in path:
                q.insert(0,i)

    return False




adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(LoopBFS(adjacency_matrix, 1))
