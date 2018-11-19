'''The following class implements two stacks with one array'''


class twoStacks:

  def __init__(self,n):
    self.size = n
    self.arr = []
    self.top1 = -1
    self.top2 = -1
    self.arr1 = self.arr[0:(self.size/2)]
    self.arr2 = self.arr[(self.size/2):]
    
                       
    
	#Insert Value in First Stack  
  def push1(self,value):
    self.top1 += 1
    self.arr1.insert(self.top1,value)
    
    return
  
	#Insert Value in Second Stack
  def push2(self,value):
    self.top2 += 1
    self.arr2.insert(self.top2,value)
    return
  
	#Return and remove top Value from First Stack
  def pop1(self):
    temp1 = self.arr1[self.top1]
    self.top1 -= 1
    return temp1
  
	#Return and remove top Value from Second Stack
  def pop2(self):
    temp2 = self.arr2[self.top2]
    self.top2 -= 1
    return temp