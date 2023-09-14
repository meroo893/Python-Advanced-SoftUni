n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))   # Creating an integer list of each row of input
    matrix.append(row)  # Adding the list into the matrix

while True:
    command = input().split()   # Reading the command
    if command[0] == "END":
        break
    x = int(command[1])  # Coordinate of the row
    y = int(command[2])  # Coordinate of the column
    if 0 <= x < n and 0 <= y < n:   # Check if the coordinates are valid
        value = int(command[3])
        if command[0] == "Add":
            matrix[x][y] += value
        elif command[0] == "Subtract":
            matrix[x][y] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(" ".join([str(x) for x in row]))  # Printing the result
    