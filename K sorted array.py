import heapq
arr = [10, 9, 8, 7, 4, 70, 60, 50]
print(arr)
k = 4
result = []

def Creating_heap(arr):
    heap = heapq.heapify(arr)
    return heapq.heappop(arr)

for i in range(len(arr)):
    print('\n', i)
    inp = arr[0:k+1]
    print('Input to heap:', inp)
    op = Creating_heap(inp)
    print('Min from heap:', op)
    
    arr.remove(op)
    
    print('main arr after : ',arr)
    
    result.append(op)
    print('sorted arr: ', result)
    
print(result)


