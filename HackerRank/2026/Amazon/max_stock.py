def getMaxStockIncrease(stockChange, k):
    max_sum = 0
    n = len(stockChange)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, min(i + k, n)):
            current_sum += stockChange[j]
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum
        
print(getMaxStockIncrease([], 6))