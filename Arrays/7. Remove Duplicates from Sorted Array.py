"""METHOD 1 """
arr = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]
new_arr=[]
i = 0
while(i<len(arr)-1):
    if arr[i]==arr[i+1]:
        new_arr.append(arr[i]) 
        i += 2
    else:
        new_arr.append(arr[i])
        i += 1  
new_arr.append(arr[len(arr)-1])           
print(new_arr)

"""METHOD 2"""
arr = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]
new2_arr = [arr[0]]
for i in range(1,len(arr)):
    if arr[i] != new2_arr[-1]:
        new2_arr.append(arr[i])
print(new2_arr)        