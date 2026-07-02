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


