
def dfs(graph, StartPoint):

    stack = [StartPoint]
    path = []

    while stack:
        current = stack.pop()    

        for i in graph[current]:
            if i not in path:
                stack.append(i)
        path.append(current)

    return path

    



adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(dfs(adjacency_matrix, 1))
