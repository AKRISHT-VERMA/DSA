"""
Problem: Move Zeroes

Pattern:
- Two Pointers

Approach:
1. Maintain an insert_position pointer.
2. Traverse the array.
3. Whenever a non-zero element is found,
   place it at insert_position.
4. Increment insert_position.
5. Fill remaining positions with 0.

Time Complexity : O(n)
Space Complexity: O(1)

----------------------------------------------------

Mistakes I Made

 Method 1

Used:

    remove()
    append()

Problems:
- Modified the list while iterating.
- remove() is O(n), leading to O(n²).
- Unsafe because elements can be skipped.

----------------------------------------------------

 Method 2

Forgot to fill remaining positions with zeroes.

Result:

[1,3,12,3,12]

instead of

[1,3,12,0,0]

----------------------------------------------------

Debugging Lesson

I accidentally tested Method 2 on the
already modified array from Method 1.

Lists are mutable.

Always reset the input before testing
another approach.

----------------------------------------------------

Interview Takeaway

Whenever I think of:

Move Zeroes

I should immediately think:

Two Pointer
Overwrite non-zero values
Fill remaining positions with zeroes

"""


"""METHOD 1 -  COMPLEXITY - O(n^2) , EXPECTED - O(n)"""
arr = [0, 1, 0, 3, 12]
for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(0)
print(arr)        

"""METHOD - 2"""
arr = [0, 1, 0, 3, 12]
insert_position = 0
for i in arr:
    if i != 0:
        arr[insert_position] = i
        insert_position += 1
while insert_position < len(arr):
    arr[insert_position] = 0
    insert_position += 1        
print(arr)        