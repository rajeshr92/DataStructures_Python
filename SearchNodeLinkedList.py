def searchNode(self, n):
        t = self.head
        while (t.nextElement != None):
            if (t.data == n):
                return True
            t = t.nextElement
        return False
