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

'''
Method - 2 (Optimal)

Problem : Set Matrix Zeroes

Pattern :
In-place Matrix Marking

Key Idea :

Instead of creating two extra sets
for rows and columns,

use

• First Row  -> Column markers
• First Column -> Row markers

The only problem is matrix[0][0]
cannot represent both the first row
and first column simultaneously.

Therefore,
we use one extra boolean variable
to remember whether the first column
originally contained a zero.

Time Complexity : O(m × n)

Space Complexity : O(1)
'''

rows = len(matrix)
cols = len(matrix[0])

# Stores whether the first column
# originally contains any zero.
first_col_zero = False


#  PASS 1 
# Mark the rows and columns
# that need to become zero.

for i in range(rows):

    # Check the original first column
    # before writing any markers.
    if matrix[i][0] == 0:
        first_col_zero = True

    # Skip first column because it is
    # being used as a row marker.
    for j in range(1, cols):

        if matrix[i][j] == 0:

            # Mark this row
            matrix[i][0] = 0

            # Mark this column
            matrix[0][j] = 0


#  PASS 2 
# Zero all cells except the
# first row and first column
# using the stored markers.

for i in range(1, rows):
    for j in range(1, cols):

        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0


#  PASS 3 
# If matrix[0][0] is zero,
# the first row must become zero.

if matrix[0][0] == 0:

    for j in range(cols):
        matrix[0][j] = 0


#  PASS 4 
# If the original first column
# contained a zero,
# make the entire first column zero.

if first_col_zero:

    for i in range(rows):
        matrix[i][0] = 0