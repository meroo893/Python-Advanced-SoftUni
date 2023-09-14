def get_key(val, my_dict):  # Get key by value
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"


n = int(input())
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # All the moves a knight can make relative to its position
board = []
knight = {}
knights_removed = 0
for _ in range(n):
    row = input()
    row_list = []
    for c in row:
        row_list.append(c)
    board.append(row_list)
"The above cycle reads the input and turns it to a n x n matrix which imitates a real life board"
while True:
    knight = {}
    for x in range(n):
        for y in range(n):
            if board[x][y] == "K":
                for move in moves:
                    x_moved = x + move[0]   # The row after moving
                    y_moved = y + move[1]   # The column after moving
                    if x_moved >= n or y_moved >= n or x_moved < 0 or y_moved < 0:  # Check if it is a legal move
                        continue
                    else:
                        if board[x_moved][y_moved] == "K":  # Check if there is a knight on the square of the move
                            try:
                                knight[(x, y)] += 1   # Attacks are increased by 1 if there is a key - value pair
                            except:
                                knight[(x, y)] = 1   # Create a key - value pair in the dictionary
    if not knight:
        break
    coordinates = get_key(max(knight.values()), knight)  # Coordinates of the knight with max number of attacks
    board[int(coordinates[0])][int(coordinates[1])] = "0"   # Removing the above-mentioned knight
    knights_removed += 1


print(knights_removed)