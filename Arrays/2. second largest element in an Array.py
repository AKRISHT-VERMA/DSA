
"""
Problem: Second Largest Element

Pattern:
- Maintain Variables

Approach:
1. Keep track of largest.
2. Keep track of second_largest.
3. If new largest appears:
      second_largest = largest
      largest = current
4. Else if current lies between them:
      update second_largest

Time Complexity : O(n)
Space Complexity: O(1)

----------------------------------------------------

Mistakes I Made

 Tried removing the largest element.

Reason:
Never modify a list while iterating.

----------------------------------------------------

 Forgot to move the old largest
into second_largest.

Missing line:

second_largest = largest

----------------------------------------------------

Important Insight

When first place changes,
the old first place becomes second place.

Think of it like a podium.

----------------------------------------------------

Edge Case

Duplicates.

Clarify whether interviewer wants

Second Largest

or

Second Distinct Largest.

"""

arr = [23, 67, 12, 89, 45, 3, 99, 54, 18, 76]
largest = arr[0]
second_largest = float('-inf')

for i in arr:
    if i > largest and i > second_largest :
        second_largest = largest
        largest = i 
    if i < largest and i > second_largest:
        second_largest = i 

print("Second largest Number : ", second_largest)      
