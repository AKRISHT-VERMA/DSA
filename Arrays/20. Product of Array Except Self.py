arr = [1, 2, 3, 4]
left_arr = [0] * len(arr)
right_arr = [0] * len(arr)
left_prod = 1
right_prod = 1
left_arr[0] = 1 
right_arr[len(right_arr)-1] = 1
result_arr = [0] * len(arr)
for i in range(1,len(arr)):
    left_prod *= arr[i-1]
    left_arr[i] = left_prod
for j in range(len(arr)-1,0,-1):
    right_prod *= arr[j]
    right_arr[j-1] = right_prod
for k in range(len(arr)):
    result_arr[k] = left_arr[k] * right_arr[k]
print(result_arr)    

