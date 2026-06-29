"""METHOD 1 -  COMPLEXITY - O(n^2) , EXPECTED - O(n)"""
arr = [0, 1, 0, 3, 12]
for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(0)
#print(arr)        

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