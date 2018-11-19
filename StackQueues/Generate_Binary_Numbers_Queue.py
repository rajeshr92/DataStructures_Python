'''findBin is a method to take every element in a queue and convert the integer into its binary representation'''

def findBin(number):
  q = myQueue(number)
  L = []
  
  for i in range(0,number):
    q.enqueue(i+1)
    
  for i in q.queueArray:  
    e = i
    quotient = 1
    t = ''
    while quotient > 0: 
    
      quotient = e//2
      r = e % 2
      t = str(r) + t
      e = quotient 
    
    L.append(t)
   
  
  return L