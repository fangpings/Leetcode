def insert(intervals, newInterval):
    if newInterval == []:
        return intervals
    if intervals == []:
        return [newInterval]
    i = 0
    while i < len(intervals) and newInterval[0] > intervals[i][1]:
        i += 1
    if i == len(intervals):
        intervals.append(newInterval)
        return intervals
    if newInterval[0] < intervals[i][0]:
        intervals.insert(i, [newInterval[0], newInterval[1]])
        if newInterval[1] < intervals[i+1][0]:
            return intervals
        tmp = intervals[i+1][1]
    else:
        tmp = intervals[i][1]
    j = i + 1
    while j < len(intervals) and newInterval[1] >= intervals[j][0]:
        tmp = intervals.pop(j)[1]
    intervals[i][1] = max(tmp, newInterval[1])
    return intervals

if __name__ == '__main__':
    print(insert([[1,5]], [0,0]))