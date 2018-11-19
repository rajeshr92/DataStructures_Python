class myQueue:
    def __init__(self,sizeOfQ):
        self.size = sizeOfQ
        self.Front = None
        self.Back = None
        self.NumberOfElements = 0
        self.myArray = []

    def isFull(self):
        if (self.NumberOfElements == (self.size-1)):
            return True

        return False

    def isEmpty(self):
        if (self.NumberOfElements == 0):
            return True

        return False

    def getTop(self):
        if (self.isEmpty()):
            print("Empty Queue")
            return
        return (self.myArray[self.Front])

    def size(self):
        return self.NumberOfElements

    def enqueue(self, dt):
        if (self.isFull()):
            print ("Queue is Full")
            return
        self.NumberOfElements += 1
        self.Back += 1
        self.myArray.insert(self.Back,dt)

        return
    
    def dequeue(self):
        if (self.isEmpty()):
            print ("Queue if empty")
            return
        self.NumberOfElements -= 1
        self.Front += 1
        
