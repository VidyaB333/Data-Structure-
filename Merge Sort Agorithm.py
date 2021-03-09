arr = [25,10,8,7,2,11,23,1]
l = 0
u = len(arr)
result = []
def MergeSort(arr):
    #global result 
    if len(arr) > 1:
        
        print('Array is : ', arr)

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        print("L :", L)
        print("R :", R)
        MergeSort(L)
        
        MergeSort(R)

        i =0
        j =0
        k =0
        
       
        while i < len(L) and j < len(R):
            print('In 1st while loop')
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            print('In while loop ,', arr)
            k+=1
        
        # Checking if any element was left 
        while i < len(L):
            print('In second loop')
            arr[k] = L[i] 
            i+=1
            k+=1
        print(i, j, k)
        while j < len(R):
            print('In third loop', j)
            arr[k] = R[j] 
            j+=1
            k+=1
        while i < len(L):
            print('Inside 2nd while loop')
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R):
            print('Inside 3rd while loop')
            arr[k] = R[j] 
            j+=1
            k+=1
  
        
def merge(arr1, arr2=[]):
    arr3 = []
    
    #arr3 = arr3 + arr1 +arr2
    arr3 = arr1 + arr2
    print("Combined array for sorting arrays: ", arr3)
    swap = False
    for i in range(0, len(arr3)):
        print('array to be sorted: ', arr3)
        for j in range(i,len(arr3)):
            if arr3[i]> arr3[j]:
                print('Before Swap :', arr3[i], arr3[j])
                arr3[i], arr3[j] = arr3[j], arr3[i]
                print('After Swap :', arr3[i], arr3[j])
                swap = True
        print('New array after ionswap : ', arr3)
            #print('in loop: ', arr3)
    if swap ==True:
        print('Swapped: ', arr3)
        

    
    print('Leaving merge funct')
    print()
    return arr3

MergeSort(arr)
