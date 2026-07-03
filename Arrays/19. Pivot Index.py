'''Method - 1 Brute force '''
arr = [1, 7, 3, 6, 5, 6]
left_sum = 0
right_sum = 0
for i in range(len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i+1:])
    if left_sum == right_sum:
        print("The pivot index is :" , i)
        break

'''Method - 2 --- Optimal Solution'''
arr = [1, 7, 3, 6, 5, 6]
left_sum = 0
right_sum = 0
found = False
total_sum = sum(arr)
for i in range(len(arr)):
    right_sum = total_sum - (left_sum + arr[i])
    if left_sum == right_sum:
        print(i)
        found = True
        break
    left_sum += arr[i]
if not found:
    print(-1)
