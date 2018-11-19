'''Below is python code to determine the number of nodes i.e. lenght of a Linked List'''


def length(list):
  h = list.getHead() ''' get the head value of the Linked List'''
  count = 0
  if (list.isEmpty()):
    return count
  else:
    
    while (h.nextElement != None):
      h = h.nextElement
      count += 1  
  return count