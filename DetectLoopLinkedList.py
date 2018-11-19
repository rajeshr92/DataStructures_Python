def detectLoop(list):
  h = list.getHead().nextElement
  L = []
  while (h.nextElement != None):
    if (h.nextElement in L):
      return True
    else: 
      L.append(h.nextElement)
      h = h.nextElement
  return False