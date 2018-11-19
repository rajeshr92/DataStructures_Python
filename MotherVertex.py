
'''
The following implementation is a method that takes a graph as an input and find out which vertex is the mother vertex in the graph.
A mother vertex is possible only in a directed graph and has a node that can traverse to all elements in the graph. 

Eg: 

graph = {
         3 -> 0 
         3 -> 1
         0 -> 1
         1 -> 2
        }

Output = 3

Explanation: We can reach all three vertices (0,1,2) if we start from 3, while in case of other vertices we can not traverse 
all of the vertices of graph e.g., If we start from vertex 0, we can only reach vertex 1 and 2 leaving out vertex 3.

The below method uses the depth first search method implemented in this repo previosly. It simply accepts a graph as input

'''

from DepthFirstSearch_Stack import dfs

def MotherVertex(g):

    k = g.keys() ''' separating the keys from the graph that is implemented as a dictionary '''
    dict = {} 
    length_value = 0
    mother_vertex = None
   
    ''' the below loop takes in each key from the dictionary and determines the path for that key as the starting point in the depth first search method '''

    for i in k:
        if i not in dict:
            dict[i] = []

        dict[i] = dfs(g,i) 

    ''' for each key, the path length is stored and compared against the previous key. The largest key is the mother vertex '''

    for i in dict:
        if length_value < len(dict[i]):
            length_value = len(dict[i])
            mother_vertex = i

    return mother_vertex
  
      
'''The below is a test case where integers in the form of a graph are passed to the MotherVertex function as a dictionary'''

adjacency_matrix = {1: [3], 2: [1, 4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

a = (MotherVertex(adjacency_matrix))

print(a)

