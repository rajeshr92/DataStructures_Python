'''Iteratively reverse a linked list'''


    def reverseLL(self):
        curr1 = self.head
        prev1 = None

        while (curr1 != None):
            currNext = curr1.nextElement
            curr1.nextElement = prev1
            prev1 = curr1
            curr1 = currNext

        self.head = prev1

        return 