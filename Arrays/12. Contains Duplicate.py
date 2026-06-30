arr = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

seen = set()
is_seen = False

for i in arr:
    if i not in seen:
        seen.add(i)
    else:
        is_seen = True
        break

print(is_seen)