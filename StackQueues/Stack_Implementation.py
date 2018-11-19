class myStack:
    def __init__(self,sizeOfArray):
        self.size = sizeOfArray
        self.myArray = []
        self.top = None

    def isEmpty(self):
        if (self.top == None):
            return True

        return False

    def isFull(self):
        if (self.top == (self.size - 1)):
            return True
        return False

    def getTop(self):
        if (self.isEmpty()):
            print ("Stack is Empty")
            return
        return self.myArray[self.top]

    def push(self,dt):
        if (self.isFull()):
            print("Stack is Full")
            return
        self.top += 1
        self.myArray.insert(self.top,dt)

        return

    def pop(self):
        if (self.isEmpty()):
            print ("Stack is Empty")
            return

        self.top -= 1