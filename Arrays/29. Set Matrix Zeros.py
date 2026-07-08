''' Method - 1 '''
matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [0, 10, 11, 12],
    [13, 14, 15, 0]
]
rows_count = len(matrix)
column_count = len(matrix[0])
rows = set()
column = set()

for i in range(rows_count):
    for j in range(column_count):
        if matrix[i][j] == 0:
            rows.add(i)
            column.add(j)
for r in rows:
    for c in range(column_count):
        matrix[r][c] = 0
for c in column :
    for r in range(rows_count):
        matrix[r][c] = 0 
print(matrix)   

