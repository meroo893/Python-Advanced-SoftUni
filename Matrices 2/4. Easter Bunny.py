n = int(input())
matrix = []
bunny_coordinates = []
best_path = []
max_eggs = 0
best_direction = ""

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for r in range(n):
    row = input().split()
    matrix.append(row)
    if "B" in row:
        bunny_coordinates.append(r)
        bunny_coordinates.append(row.index("B"))

for direction, offset in directions.items():
    row, col = bunny_coordinates[0] + offset[0], bunny_coordinates[1] + offset[1]
    path = []
    eggs = 0

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break

        eggs += int(matrix[row][col])
        path.append([row, col])

        row += offset[0]
        col += offset[1]

    if eggs >= max_eggs:
        max_eggs = eggs
        best_direction = direction
        best_path = path


print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)