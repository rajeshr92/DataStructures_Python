''' searchNode is a method implemented using Python scan through a given Linked List and return a boolean whether if an element exists or not
the logic is a loop algorithm that accepts a search criteria'''

def searchNode(self, n):
        t = self.head
        while (t.nextElement != None):
            if (t.data == n):
                return True
            t = t.nextElement
        return False
