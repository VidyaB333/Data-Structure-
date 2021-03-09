arr= [64, 25, 12, 22,11, 1,44]

def Bubble_Sort(arr, n):
    
    for j in range(n):
        swap= False
        print('*** {} th pass'.format(j))
        for i in range(0, n-j-1):
            if arr[i]>arr[i+1]:
                #print(arr[i], arr[i+1])
                arr[i], arr[i+1]= arr[i+1], arr[i]
                print(arr[i], arr[i+1])
                swap= True
            print(arr)
        if swap ==False:
            break
    print(arr)

Bubble_Sort(arr, len(arr))
