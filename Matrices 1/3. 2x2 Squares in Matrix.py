rc = list(map(int, input().split()))
rows = rc[0]
columns = rc[1]
matrix = []
two_by_twos = 0
for _ in range(rows):
    row = input().split(" ")
    matrix.append(row)

for row_index in range(rows-1):
    for col_index in range(columns-1):
        if matrix[row_index][col_index] == matrix[row_index + 1][col_index] == matrix[row_index][col_index+1]\
                == matrix[row_index + 1][col_index + 1]:
            two_by_twos += 1

print(two_by_twos)
