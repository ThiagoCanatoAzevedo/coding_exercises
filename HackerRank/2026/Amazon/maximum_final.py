def maximumFinal(arr):
    arr.sort()
    arr[0] = 1

    for i in range(len(arr)):
        arr[i] = min(arr[i], arr[i-1]+1)
    
    return arr[-1]



    
print(maximumFinal([3,1,7,10,8]))
