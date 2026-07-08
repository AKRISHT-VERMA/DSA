intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals.append(newInterval)
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


'''METHOD - 2 OPTIMAL SOLUTION'''

'''
Problem : Insert Interval

Pattern : Interval Merging

Key Idea :

The intervals are already sorted.

There are only three possibilities.

1. Current interval comes before newInterval.
2. Current interval overlaps with newInterval.
3. Current interval comes after newInterval.

Instead of maintaining a current interval,
we keep merging into newInterval itself.

Time Complexity : O(n)

Space Complexity : O(n)
'''

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

result = []

for interval in intervals:

    # Case 1
    if interval[1] < newInterval[0]:
        result.append(interval)

    # Case 2
    elif interval[0] > newInterval[1]:

        result.append(newInterval)

        newInterval = interval

    # Case 3
    else:

        newInterval[0] = min(newInterval[0], interval[0])
        newInterval[1] = max(newInterval[1], interval[1])

result.append(newInterval)

print(result)