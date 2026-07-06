arr = [1, 3, 2]

# Step 1: Find the pivot
pivot = -1

for i in range(len(arr) - 2, -1, -1):
    if arr[i] < arr[i + 1]:
        pivot = i
        break

# Step 2: If no pivot exists, reverse the whole array
if pivot == -1:
    arr.reverse()

else:
    # Step 3: Find the smallest element greater than pivot
    for i in range(len(arr) - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Step 4: Reverse everything after the pivot
    left = pivot + 1
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

print(arr)