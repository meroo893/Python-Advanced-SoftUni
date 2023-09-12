rc = list(map(int, input().split()))
rows = rc[0]
columns = rc[1]
matrix = []
for _ in range(rows):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

max_sum = -9999999999999
max_matrix = [[], [], []]
for row_index in range(rows-2):
    for col_index in range(columns - 2):
        three_by_three_sum = 0
        three_matrix = [[], [], []]
        for i in range(3):
            for j in range(3):
                three_by_three_sum += matrix[row_index + i][col_index + j]
                three_matrix[i].append(matrix[row_index + i][col_index + j])

        if three_by_three_sum > max_sum:
            max_sum = three_by_three_sum
            max_matrix = three_matrix


print(f"Sum = {max_sum}")
for row in max_matrix:
    print(' '.join([str(x) for x in row]))