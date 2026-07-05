arr = [4,3,2,7,8,2,3,1]
seen = set()
missing_numbers = []
for i in arr:
    seen.add(i)
for i in range(1,len(arr)+1):
    if i not in seen:
        missing_numbers.append(i)
print(missing_numbers)          