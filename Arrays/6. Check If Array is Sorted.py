arr = [5, 9, 14, 21, 32, 45, 58, 72]
is_sorted = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break
if is_sorted == True:
    print("The given Array:", arr , "is sorted")
else:
    print("The given Array :", arr , "is not sorted")    
