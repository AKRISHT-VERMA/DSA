s = "anagram"
t = "nagaram"
frequency_s = {}
frequency_t = {}
for i in s :
    if i not in frequency_s :
        frequency_s[i] = 1
    else :
        frequency_s[i] += 1
for j in t:
    if j not in frequency_t:
        frequency_t[j] = 1
    else:
        frequency_t[j] += 1
if frequency_s == frequency_t:
    print(True)
else:
    print(False)                         
