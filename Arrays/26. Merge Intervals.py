intervals = [[1,3],[2,6],[5,8],[10,12]]

intervals.sort()
current_interval = intervals[0]
result = []

for i in range(len(intervals)-1):
    if current_interval[1] >= intervals[i+1][0]:
        current_interval[0] = min(current_interval[0],intervals[i+1][0])
        current_interval[1] = max(current_interval[1],intervals[i+1][1])
    else:
        result.append(current_interval)
        current_interval = intervals[i+1]
result.append(current_interval)
print(result)       

