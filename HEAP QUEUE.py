import heapq
l = [10,5,8,22,11,800,4]
print(l)
heapq.heapify(l)
print(l)
heapq.heappush(l,55)
heapq.heappush(l,5)
heapq.heappush(l,25)
heapq.heappush(l,9)
heapq.heappush(l,3)

print(l)
heapq.heapify(l)
print(l)
heapq.heappop(l)
print(l)
heapq.heappushpop(l,20)
print(l)
heapq.heapreplace(l,3)
print(l)


