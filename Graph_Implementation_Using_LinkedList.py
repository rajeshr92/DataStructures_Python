from LinkedList import LinkedList

class graph:
    
    def __init__(self):
        self.dic = {}
    
    def createDic(self,v):
        temp = LinkedList()
        self.dic[v] = temp
        return
    
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