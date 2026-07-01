arr = [2, 2, 1, 1, 1, 2, 2]
frequency = {}
for element in arr:
    if element not in frequency:
        frequency[element] = 1
    else:
        frequency[element] += 1     

    if frequency[element] > len(arr)//2 :
        print("Number :", element , "appears :" , frequency[element] , "times")    
        break 

