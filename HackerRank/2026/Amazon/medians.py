def medians(values, k):
    values.sort()
    n = len(values)
    m = (k - 1) // 2

    min_median = values[m]
    max_median = values[n - k + m]

    return [max_median, min_median]
                

print(medians([1,2, 3], 2))