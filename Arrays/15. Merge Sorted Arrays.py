'''Problem:
Merge Sorted Array

Pattern:
Two Pointers

Difficulty:
Easy

----------------------------------------------------

Approach

Maintain two pointers.

i → arr1

j → arr2

Compare the current elements.

Append the smaller one.

Move only that pointer.

When one array finishes,

copy the remaining elements
from the other array.

----------------------------------------------------

Time Complexity

O(m+n)

----------------------------------------------------

Space Complexity

O(m+n)

(using a new array)

----------------------------------------------------

## Mistakes I Made ##

 Initially tried using a set.

Problem:

Sets remove duplicates.

This problem requires
keeping duplicates.

-------------------------------------

 Tried one pass of swapping.

Problem:

One Bubble Sort pass
cannot completely sort
an array.

-------------------------------------

 Compared leftover pointers
with the wrong limits.

Correct:

i < m

j < n

----------------------------------------------------

Key Insight

Only move the pointer
of the array whose element
you copied.

----------------------------------------------------

Pattern Learned

Merge Two Sorted Arrays'''
arr1 = [1, 2, 3, 0, 0, 0]
m = 3
arr2 = [2, 5, 6]
n = 3
j = i = 0
sorted_array = []
while(i<m and j<n):
    if arr1[i] <= arr2[j]:
        sorted_array.append(arr1[i])
        i += 1
    else:
        sorted_array.append(arr2[j])
        j += 1
while(j<n):
    sorted_array.append(arr2[j])
    j += 1
while(i<m):
    sorted_array.append(arr1[i])
    i += 1
print(sorted_array)                        


