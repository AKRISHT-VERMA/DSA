arr = [-7, -3, 2, 3, 11]
left = 0
right = position = len(arr) - 1
result_arr = [0] * len(arr)
while left <= right:
    if (arr[left]**2) <= (arr[right]**2):
        result_arr[position] = arr[right]**2
        position -= 1
        right -= 1
    else:
        result_arr[position] =arr[left]**2
        position -= 1
        left += 1
print(result_arr)            

