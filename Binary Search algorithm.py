arr = [ 2, 3, 4,5,6,7,8,10, 11,23,40 , 45,55,60]
x = 9

def binary_search(arr, l, u,x):
    print(l, u)
    if u>=l:
        
        midpoint = l + (u -l)//2
        print('again {}, {}, {},{}'.format(arr, l, u, midpoint))

        if arr[midpoint] == x:
            print('at midpoint')
            return midpoint

        elif x > arr[midpoint]:
            return binary_search(arr,  midpoint + 1, u, x)

        elif x < arr[midpoint]:
            return binary_search(arr, l, midpoint -1, x)

    else :
        return -1
result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")


