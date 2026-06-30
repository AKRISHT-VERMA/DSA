'''METHOD - 1'''
arr = [3, 2, 2, 3, 4, 2, 5]
val = 2
new_arr = []
for i in arr:
    if i != val:
        new_arr.append(i)
print(new_arr)        

'''METHOD - 2'''
arr = [3, 2, 2, 3, 4, 2, 5]
val = 2
insert_position = 0
for i in arr:
    if i != val:
        arr[insert_position] = i
        insert_position += 1
print(arr)                
