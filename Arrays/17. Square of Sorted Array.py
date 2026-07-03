'''Problem:
Squares of a Sorted Array

Pattern:
Two Pointers

----------------------------------------------------

Approach

Keep one pointer at the left end.

Keep one pointer at the right end.

The largest square is always at
one of the two ends.

Compare both squares.

Place the larger square at the
last empty position of the
result array.

Move only the pointer whose
square was used.

Repeat until the pointers cross.

----------------------------------------------------

Time Complexity

O(n)

Reason

Each pointer moves only forward
(or backward) once.

Every element is processed once.

----------------------------------------------------

Space Complexity

O(n)

Reason

A new result array is created.

----------------------------------------------------

Key Insight

The largest square is not
necessarily from the largest
number.

It comes from the largest
absolute value.

----------------------------------------------------

Mistake I Made

Initially thought of

Square everything

↓

Sort

Later realized

Sorting is unnecessary because
the largest square always lies
at one of the two ends.

----------------------------------------------------

Pattern Reinforced

Two Pointers'''

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

