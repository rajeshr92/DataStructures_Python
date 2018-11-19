
'''removeDuplicates is a method to remove repeating elements in a linked list. The logic used was creating a list to append all the visited elements and iteratively checking the list for repetition'''

def removeDuplicates(list):
  h = list.getHead().nextElement
  curr = h
  L = []
  prev = None
  while (curr != None):
    
    if (curr.data in L):
      prev.nextElement = curr.nextElement
      curr = curr.nextElement
    else:
      L.append(curr.data)
      prev = curr
      curr = curr.nextElement
      
      
  return