arr = [64,25,12,22,11]

def Selection_Sort(arr, n):
   for i in range(n):
       min_idx = i
       for j in range(i+1, n):
           if arr[min_idx] > arr[j]: 
               min_idx= j
               print(arr[min_idx])
       arr[i], arr[min_idx] = arr[min_idx], arr[i]


print(Selection_Sort(arr, len(arr)))
print(arr)
