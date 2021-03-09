lst = [23,4,55,0,-1,22,12,3,14]

def search(lst, num):
    for i in range(0, len(lst)):
        if num == lst[i]:
            #index = lst.index(num)
            return i
            print('Number exist')
    return -1
            
n1, n2 = 12,2               
print('{} is present in {} at index :{}'.format(n1,lst, search(lst, n1), lst))
print('{} is present in {} at index : {}'.format(n2, lst, search(lst, n2), lst))
