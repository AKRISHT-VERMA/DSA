"""
Problem: Check if Array is Sorted

Pattern:
- Linear Traversal
- Boolean Flag

Approach:
Assume array is sorted.

Look only for evidence that proves
it is NOT sorted.

If arr[i] > arr[i+1]:
    Not Sorted

Break immediately.

Time Complexity : O(n)
Space Complexity: O(1)

----------------------------------------------------

Mistakes I Made

 Reset is_sorted=True inside loop.

Once array becomes unsorted,
it should never become sorted again.

----------------------------------------------------

Important Insight

Don't ask:

Is this pair sorted?

Ask:

Did I find a pair that breaks sorting?

"""

arr = [5, 9, 14, 21, 32, 45, 58, 72]
is_sorted = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break
if is_sorted == True:
    print("The given Array:", arr , "is sorted")
else:
    print("The given Array :", arr , "is not sorted")    
