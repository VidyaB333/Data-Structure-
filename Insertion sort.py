arr = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
print(arr)
n = len(arr)
def Insertion_sort(arr, n):
    for i in range(1, n):
        #print('fot  i ', arr[i])
        for j in range(0, i):
            #print(arr[j], arr[i])
            if arr[i]< arr[j]:
                temp = arr[i]
                del arr[i]
                arr.insert(j, temp)
                #print('swap done', arr)
        #print(arr)
    return arr

op = Insertion_sort(arr, n)
print(op)
