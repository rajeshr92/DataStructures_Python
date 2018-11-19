'''reverseK is a method that takes a queue and the integer 'k' and reverses the first 'k' elements of the queue. 

Eg:

  Queue = {1,2,3,4,5,6,7,9,10}    k = 5
  Output = {5,4,3,2,1,6,7,8,9,10}

'''

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