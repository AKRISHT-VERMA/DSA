'''Method - 1'''
arr = [9,6,4,2,3,5,7,0,1]
seen = set()
for number in arr:
    # if number not in seen: 
    '''Above line is not required as set automatically stores only unique value'''
    seen.add(number)
for missin_no in range(len(arr)+1):
    if missin_no not in seen:
        print("The Missing Number is :", missin_no)
        break      

'''Method - 2 -- Mathematical Approach''' 
arr = [9,6,4,2,3,5,7,0,1]
n = len(arr)
missing_no = ((n*(n+1))//2) - sum(arr)
print(missing_no)