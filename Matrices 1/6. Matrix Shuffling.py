rc = list(map(int, input().split()))
rows = rc[0]
columns = rc[1]
matrix = []
for _ in range(rows):
    row = input().split(" ")
    matrix.append(row)


while True:
    command = input().split()
    if command[0] == "END":
        break
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    else:
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
        if x1 >= rows or x2 >= rows or y1 >= columns or y2 >= columns:
            print("Invalid input!")
        else:
            value = matrix[x1][y1]
            matrix[x1][y1] = matrix[x2][y2]
            matrix[x2][y2] = value
            for row in matrix:
                print(' '.join([str(x) for x in row]))
