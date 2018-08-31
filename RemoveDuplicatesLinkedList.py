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