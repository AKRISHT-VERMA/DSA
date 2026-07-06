'''Method - 1'''
arr = [2, 0, 2, 1, 1, 0]
arr_0 = []
arr_1 = []
arr_2 = []
resultant_arr = []
for i in arr:
    if i == 0 :
        arr_0.append(i)
    elif i == 1:
        arr_1.append(i)
    else:
        arr_2.append(i)    
resultant_arr = arr_0 + arr_1 + arr_2
print(resultant_arr)        

'''Method - 2'''
arr = [2, 0, 2, 1, 1, 0]
count_0 = 0
count_1 = 0
count_2 = 0
resultant_arr = []
for i in arr:
    if i == 0 :
        count_0 += 1
    elif i == 1:
        count_1 += 1
    else:
        count_2 += 1    
resultant_arr = [0] * count_0 + [1] * count_1 + [2] * count_2
print(resultant_arr)        


