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
