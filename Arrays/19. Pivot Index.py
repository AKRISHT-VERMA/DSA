arr = [1, 7, 3, 6, 5, 6]
left_sum = 0
right_sum = 0
for i in range(len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i+1:])
    if left_sum == right_sum:
        print("The pivot index is :" , i)
        break