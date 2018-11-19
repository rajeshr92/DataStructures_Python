''' Below is an implementation of LinkedList ussing the Node class and LinkedList class. Basic operations of a linked list such insertion, deletion, and printing are implemented as methods within the LinkedList class
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def insertAthead(self,d):
        temp = Node(d)
        temp.nextElement = self.head
        self.head= temp
        return self.head

    def isEmpty(self):
        if (self.head.nextElement == None):
            return True
        else:
            return False

    def insertAtend(self,d):
        new = Node(d)
        t = self.head
        while (t.nextElement != None):
            t = t.nextElement

        t.nextElement = new

        return '''self.printList()'''
    
    def insertAtPostion(self,d,pos):
        new = Node(d)
        t = self.head
        prev = None
        curr = t
        increment = 0
        while (increment < pos) and curr.nextElement:
            prev = curr
            curr = curr.nextElement
            increment += 1
            
        prev.nextElement = new
        new.nextElement = curr

        return self

    def deletionAtHead(self):
        h = self.head
        self.head = h.nextElement
        h = None

        return

    def deleteAtpos(self,dt):
        
        h = self.head
        prev = None
        curr = h

        while (curr != None):
            
            if (curr.data == dt):
                prev.nextElement = curr.nextElement
                newCurr = curr.nextElement
                curr = None
                break
            
                
            prev = curr
            curr = curr.nextElement

            if (curr == None):
                print("Element not in LL")
                return

        return self.printList()
        

    def printList(self):
        if (self.isEmpty()):
            print("List is empty")
            return False
        
        t = self.head
        while (t != None):
            print (t.data)
            t = t.nextElement

        return True