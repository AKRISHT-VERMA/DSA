arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(arr)
result_arr = [0]*k
i = 0
j = k-1
while(i<k):
    result_arr[j] = arr.pop()
    j -= 1
    i += 1
result_arr += arr
print(result_arr)    