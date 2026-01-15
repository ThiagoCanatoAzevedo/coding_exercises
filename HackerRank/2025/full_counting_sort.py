def countingSort(arr: list):
    result = []
    
    for i in range(len(arr)//2):
        arr[i][1] = "-"
    
    arr = sorted(arr)
    
    for i in range(int(len(arr))):
        result.append(arr[i][1])
        
    print(' '.join(result))
    
countingSort([[0,"a"],[1,"b"],[0,"c"], [1,"d"]])

"""
Exercise anotations:
- Name: The Full Counting Sort
- Difficulty: Medium
- Score: 40/40
"""