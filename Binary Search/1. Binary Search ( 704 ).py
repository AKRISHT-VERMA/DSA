nums = [-1,0,3,5,9,12]
target = 9

found  = False
low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] < target :
        low = mid + 1

    elif nums[mid] > target :
        high = mid - 1    

    else :
        print("The index of Target elemnt", target , "is :" , mid)
        found = True
        break
if not found:
     print("Target Element was not found")