def reverseK(queue,k):
  L = []
  LL = []
  for i in range(k):
    L.append(queue.dequeue())
    i += 1
  
  for i in range(len(queue.queueArray)):
    LL.append(queue.dequeue())
    i += 1
  
  for i in range((len(L)//2)):
    temp = L[i]
    L[i] = L[len(L)-i-1]
    L[len(L)-i-1] = temp
  
  L = L + LL
  
  for i in L:
    queue.enqueue(i)
    
  
    
    
  return 