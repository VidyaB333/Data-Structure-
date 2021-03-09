
arr=[38,34,22,55,63,22,4,11,2,33,44,55]

def shell_sort(arr, gap):
    print(gap)

    if gap==1:
        for i in range(len(arr)):
            for j in range(i):
                if arr[i]<arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            print(i , arr)
        print(arr)
        return arr

    for i in range(len(arr)-gap):
        j= i+gap
        if arr[i]> arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        m= i-gap
        if m>=0:
            if arr[i] < arr[m]:
                arr[i], arr[m] = arr[m], arr[i]
        print(arr)

    gap = gap//2
    print('*****')
    shell_sort(arr, gap)


gap =len(arr)//2
sorted = shell_sort(arr, gap)
print(sorted)
