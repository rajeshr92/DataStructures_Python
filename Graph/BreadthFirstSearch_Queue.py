'''
The following is a breadth first implementation using queue data strcuture. 

'bfs' function accepts two arguments; a graph represented in the form of a dictionary and a starting point for the graph to start the breadth first search 
'''

def bfs(graph, StartPoint):

    q = [StartPoint] ''' a queue that is initilized with the starting point '''
    path = [] ''' an empty list to document the path as the program traverses through the graph '''

    while q:

        current = q.pop()

        path.append(current) '''appending the element to path after being visited'''

        for i in graph[current]:
            if i not in q:
                q.insert(0,i) '''taking elements/integers from the graph and queueing it to the queue 'q' only after checking if it is a parent node that has already been visited'''

    return path



'''The below is a test case where integers in the form of a graph are passed to the bfs function as a dictionary'''

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(bfs(adjacency_matrix, 1))
