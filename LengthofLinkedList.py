def length(list):
  h = list.getHead()
  count = 0
  if (list.isEmpty()):
    return count
  else:
    
    while (h.nextElement != None):
      h = h.nextElement
      count += 1  
  return count