arr = [1, 2, 3]

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


'''
Problem : Next Permutation

Key Idea

We have to find the smallest permutation
that is just greater than the current one.

Step 1
Traverse from right to left.

Find the first element where

arr[i] < arr[i+1]

This is the first position from the right
where the current permutation can be increased.

Step 2

Find the smallest element greater than
arr[i] on its right side.

Swap both elements.

Step 3

Reverse everything after that position.

Reason:

The right side is always in descending order.

Reversing it makes it ascending,
which gives the smallest possible permutation.

Time Complexity : O(n)

Space Complexity : O(1)
'''