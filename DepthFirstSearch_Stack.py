
'''
The following is a depth first implementation using stack data strcuture. 
'dfs' function accepts two arguments; a graph represented in the form of a dictionary and a starting point for the graph to start the breadth first search 
'''

def dfs(graph, StartPoint):

    stack = [StartPoint] ''' a stack that is initilized with the starting point '''
    path = [] ''' an empty list to document the path as the program traverses through the graph '''

    while stack:
        current = stack.pop()    

        for i in graph[current]:
            if i not in path:
                stack.append(i) '''taking elements/integers from the graph and stacking it to the stack 'stack' only after checking if it is a parent node that has already been visited'''
        path.append(current)  '''appending the element to path after being visited'''

    return path

    


'''The below is a test case where integers in the form of a graph are passed to the bfs function as a dictionary'''

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(dfs(adjacency_matrix, 1))
