n = int(input())
matrix = []
main_diagonal = []
sec_diagonal = []

for _ in range(n):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

row_index = 0
for row in matrix:
    column_index = 0
    for value in row:
        if row_index == column_index:
            main_diagonal.append(value)
        if row_index + column_index == n-1:
            sec_diagonal.append(value)
        column_index += 1
    row_index += 1

#print(f"Primary diagonal: {', '.join([str(x) for x in main_diagonal])}. Sum: {sum(main_diagonal)}")
#print(f"Secondary diagonal: {', '.join([str(x) for x in sec_diagonal])}. Sum: {sum(sec_diagonal)}")

print(abs(sum(sec_diagonal) - sum(main_diagonal))) #2ra zadacha
