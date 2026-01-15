def findOverlappingTimes(intervals):
    intervals.sort()
    result = []
    
    inicio = intervals[0][0]
    fim = intervals[0][1]
    for i in range(1, len(intervals)):
        if fim >= intervals[i][0]:
            fim = max(fim, intervals[i][1])
        else:
            result.append([inicio, fim])
            inicio = intervals[i][0]
            fim = intervals[i][1]
            
    result.append([inicio, fim])
    return result
findOverlappingTimes([[7,7],[2,3],[6,11], [1,2]])