def smallestIndex(nums):
    for i, n in enumerate(nums):
        list_n = list(map(int, str(n)))
        sum_list_n = sum(list_n)
        if sum_list_n == i:
            return i

    return -1

print(smallestIndex([1,10,11]))
