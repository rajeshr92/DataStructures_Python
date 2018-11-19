def findMid(list):
  
  h = list.getHead().nextElement
  L = []
  while (h.nextElement != None):
    L.append(h.data)
    h = h.nextElement
  a = len(L)//2
  b = L[a]
  
  
  return b