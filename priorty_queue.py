#Priority Queue using List
#Inserion rtakes 0(n) time
l =[]
l.append((3,'drink'))
l.append((1,'food'))
l.append((2, 'sleep'))
l.append((4, 'beath'))


print(l.sort(reverse= True))
print(l)
while(l):
    print(l.pop(0))

#Priority Queue using heapq module
import heapq
lst = [(2,'b'),(6,'f'),(1,'a')]
heap = heapq.heapify(lst)
print(lst)
print(heapq.heappop(lst))
print(heapq.heappush(lst,(4,'d')))
print(lst)
print(heapq.heappushpop(lst,(5,'e')))
print(lst)
print(heapq.heapreplace(lst,(10,'i')))
print(lst)


#Using queue.PriorityQueue class
from queue import PriorityQueue

q = PriorityQueue()
q.put((10,'ten'))
q.put((1,'One'))
q.put((2,'Two'))
q.put((4,'Four'))
print(q.get())


print()
#Using List and OOPS Concept
class Node:
  def __init__(self, info, priority):
    self.info = info
    self.priority = priority
    
#class for Priority queue 
class PriorityQueue:
  def __init__(self):
    self.queue = list()
    # if you want you can set a maximum size for the queue
    
  def insert(self, node):
    # if queue is empty
    if self.size() == 0:
      # add the new node
      self.queue.append(node)
    else:
      # traverse the queue to find the right place for new node
      for x in range(0, self.size()):
        # if the priority of new node is greater
        if node.priority >= self.queue[x].priority:
          # if we have traversed the complete queue
          if x == (self.size()-1):
            # add new node at the end
            self.queue.insert(x+1, node)
          else:
            continue
        else:
          self.queue.insert(x, node)
          return True
  
  def delete(self):
    # remove the first node from the queue
    return self.queue.pop(0)
    
  def show(self):
    for x in self.queue:
      print(str(x.info)+" - "+str(x.priority))
  
  def size(self):
    return len(self.queue)

pQueue = PriorityQueue()
node1 = Node("C", 3)
node2 = Node("B", 2)
node3 = Node("A", 1)
node4 = Node("Z", 26)
node5 = Node("Y", 25)
node6 = Node("L", 12)

pQueue.insert(node1)
pQueue.insert(node2)
pQueue.insert(node3)
pQueue.insert(node4)
pQueue.insert(node5)
pQueue.insert(node6)
pQueue.show()
print("--------")
pQueue.delete()
pQueue.show()









