matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = len(matrix)
cols = len(matrix[0])
top = 0 
bottom = rows - 1
left = 0
right = cols - 1
spiral = []

while top <= bottom and left <= right:
    # TOP ROW
    for c in range(left, right+1):
        spiral.append(matrix[top][c])
    top += 1
    # RIGHT COLUMN
    for r in range(top , bottom + 1):
        spiral.append(matrix[r][right])
    right -= 1
    # BOTTOM ROW 
    if top <= bottom :
       for c in range(right, left - 1, -1):
           spiral.append(matrix[bottom][c])
       bottom -= 1
    # LEFT COLUMN
    if left <= right:
        for r in range(bottom , top - 1 , -1):
            spiral.append(matrix[r][left])
        left += 1

print(spiral)                
        
        

