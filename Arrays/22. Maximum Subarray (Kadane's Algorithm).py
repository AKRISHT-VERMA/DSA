arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current_sum = max_sum = arr[0]
for i in range(1,len(arr)):
    if current_sum + arr[i] > arr[i] :
        current_sum += arr[i]
    else:
        current_sum = arr[i]
    if max_sum < current_sum :
        max_sum = current_sum 
print(max_sum)                