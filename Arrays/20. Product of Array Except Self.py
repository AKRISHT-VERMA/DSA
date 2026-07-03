'''Problem:
Product of Array Except Self

Pattern:
Prefix Product

Difficulty:
Medium

----------------------------------------------------

Approach

Create Left Product array.

Create Right Product array.

Left Product

stores the product of all
elements before the current index.

Right Product

stores the product of all
elements after the current index.

Multiply both arrays.

----------------------------------------------------

Time Complexity

O(n)

Reason

Three sequential traversals.

----------------------------------------------------

Space Complexity

O(n)

----------------------------------------------------

Key Insight

Instead of recalculating products,

maintain

Left Product

and

Right Product

separately.

----------------------------------------------------

Mistake I Almost Made

Thought traversing from the
right would not work.

Reality

Dry running the algorithm
proved it worked perfectly.'''

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

