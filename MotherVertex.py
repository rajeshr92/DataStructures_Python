from DepthFirstSearch_Stack import dfs

def MotherVertex(g):

    k = g.keys()
    dict = {}
    length_value = 0
    mother_vertex = None

    for i in k:
        if i not in dict:
            dict[i] = []

        dict[i] = dfs(g,i)

    for i in dict:
        if length_value < len(dict[i]):
            length_value = len(dict[i])
            mother_vertex = i

    return mother_vertex
        

adjacency_matrix = {1: [3], 2: [1, 4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

a = (MotherVertex(adjacency_matrix))

print(a)

