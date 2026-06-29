arr = [2, 7, 11, 15]
target = 9
seen = {}
for i in range(len(arr)):
    if target - arr[i] in seen:
        print(seen[target-arr[i]],i)
        break
    else:
        seen[arr[i]] = i    
