"""
Problem:
Two Sum

Pattern Used:
Hashing
Complement Search

Difficulty:
Easy

----------------------------------------------------

Approach

For every element,

1. Compute the complement.

complement = target-current

2. Check whether complement
already exists inside the dictionary.

3. If yes,
return the stored index and
current index.

4. Otherwise,
store the current number
along with its index.

----------------------------------------------------

Time Complexity

O(n)

Dictionary lookup

O(1)

----------------------------------------------------

Space Complexity

O(n)

----------------------------------------------------

Mistakes I Made

 Initially searched the list using

target-current in arr

This made searching O(n).

----------------------------------------------------

 Used arr.index()

Forgot that i already stores
the index.

----------------------------------------------------

Key Insight

Instead of asking

Which two numbers add to target?

Ask

What number do I need
to reach the target?

This number is called

Complement.

----------------------------------------------------

Debugging Lesson

Dictionary stores

Number → Index

Example

{

2 : 0,

7 : 1,

11 : 2

}

Whenever complement is found,

seen[complement]

directly gives the answer.

----------------------------------------------------

Interview Takeaway

Whenever a problem asks

Find pair

Find complement

Find previous occurrence

Think

HashMap (Dictionary)

"""

arr = [2, 7, 11, 15]
target = 9
seen = {}
for i in range(len(arr)):
    if target - arr[i] in seen:
        print(seen[target-arr[i]],i)
        break
    else:
        seen[arr[i]] = i    
