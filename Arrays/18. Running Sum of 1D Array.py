arr = [5, 10, 2, 8]
result_arr = [0] * len(arr)
result_arr[0] = arr[0]
i = 1
while(i<len(arr)):
    result_arr[i] = result_arr[i-1] + arr[i]
    i += 1
print(result_arr)    