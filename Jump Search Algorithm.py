import math

arr = [2, 3, 4, 10, 40, 45,55,60]
x = 60
n = len(arr)
m = int(math.sqrt(n))

def jump_search(arr,n, m, x):
    start = 0
    end = m
    while (arr[n-1]>=x) & (end<n):
        
        start = end
        end = end + m
        print(start, end)
        
        if (end >(n-1)):
            end= n
         
jump_search(arr,n, m, x)









    
"""
    for i in range(0, n, m):
        print(arr[i])
        if arr[i] ==x:
            return i
        elif arr[i] > x:
            print('For Linear Seach')
            L = i-m
            R = i
            for i in range(L, R+1):
                if arr[i]==x:
                    return i
    return -1

result = jump_search(arr, n, m , x)
if result !=-1:
    print('{} is at {} index in {}'.format(x, result, arr))
else:
    print('{} is not in {}'.format(x, arr))"""
        
    
