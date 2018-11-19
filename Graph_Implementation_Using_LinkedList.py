''' 
Graph can be represented in many forms. While the problem statement determines the best form of repsentation, the code below represents graph using a Linked List data structure. 
The code also has methods to create, add, and print elements and edges in the bi-directional graph
'''

from LinkedList import LinkedList ''' Python syntax to inherit other classes '''

class graph:
    
    def __init__(self):
        self.dic = {}

    ''' createDic method will assign objects of the LinkedList class i.e. temp to each parent node i.e. key in the dictionary '''    

    def createDic(self,v):
        temp = LinkedList()
        self.dic[v] = temp
        return

    ''' Add_Edge is a method to add elements to the graph for a given parent node using the methods within the LinkedList() class '''
    
    def Add_Edge(self,u,v):
        self.dic[u].insertAthead(v)
        return
    
    def PrintEdges(self,u):
        h = self.dic[u].head
        
        while (h != None):
            print(h.data)
            
            h = h.next
        
        return
    
    def printdic(self):
        print(self.dic.keys())
        return