
'''
The following implementation is a method that takes a graph as an input and detects a cycle/loop in it. Eg: 

graph = {
	 0 -> 1 
         1 -> 2
         2 -> 0
        }

LoopBFS is a breadth first search that accepts a graph and a starting point
'''

def LoopBFS(graph, StartPoint):

    q = [StartPoint]
    path = []

    while q:

        current = q.pop()

        path.append(current)

        for i in graph[current]:
            if i in path: ''' checking if the node is point back to a prevously visited node '''
                return True
            elif i not in path:
                q.insert(0,i) ''' appending the node element to keep a log of all the visited nodes '''

    return False



'''The below is a test case where integers in the form of a graph are passed to the LoopBFS function as a dictionary'''

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(LoopBFS(adjacency_matrix, 1))
