arr = [23, 67, 12, 89, 45, 3, 99, 54, 18, 76]
max_element = min_element = arr[0]
for i in arr :
    if max_element<i:
        max_element = i
    if min_element>i:
        min_element = i 
print("Maximum :" , max_element)
print("Minimum :" , min_element)    