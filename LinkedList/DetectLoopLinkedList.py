'''detectLoop is a method to detect a loop in a linked list; a loop is any reference to a previous node in a linked list.'''

def detectLoop(list):
  h = list.getHead().nextElement
  L = [] ''' an empty list to keep tab of visited elements in a linked list '''
  while (h.nextElement != None):
    if (h.nextElement in L):
      return True
    else: 
      L.append(h.nextElement)
      h = h.nextElement
  return False