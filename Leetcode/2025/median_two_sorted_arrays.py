def findMedianSortedArrays(nums1, nums2):
    nums1_2 = sorted(nums1+nums2)
    if len(nums1_2) % 2 != 0:
        indice = int(len(nums1_2)/2)
        return(nums1_2[indice])
    else:
        first_ind = int(len(nums1_2)/2)
        second_ind = first_ind - 1
        return (nums1_2[first_ind] + nums1_2[second_ind])/2.0
    
    """
    Must use 2.0 to divide because Python's version. 
    Probably, in Leetcode they use Python 2.0 and, in this version, when you divide by 2, it gives you an integer number, not a float
    """
    
print(findMedianSortedArrays([1,2], [3,4]))
"""
Exercise annotations:
- Name: Median of Two Sorted Arrays
- Runtime: 1ms
- Memory: 12.60MB
"""