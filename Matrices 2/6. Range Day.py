territory = []
targets_hit = []
targets = 0
directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}
x = 0
y = 0
for r in range(5):
    row = input().split()
    territory.append(row)
    if "A" in row:
        x = r
        y = row.index("A")
    targets += row.count("x")

for _ in range(int(input())):
    command = input().split()
    if command[0] == "move":
        direction = command[1]
        amount = int(command[2])
        x += directions[direction][0] * amount
        y += directions[direction][1] * amount
        if x >= 5 or x < 0 or y >= 5 or y < 0:
            x -= directions[direction][0] * amount
            y -= directions[direction][1] * amount
        elif territory[x][y] != ".":
            x -= directions[direction][0] * amount
            y -= directions[direction][1] * amount
    else:
        direction = command[1]
        bullet_x = x
        bullet_y = y
        while True:
            bullet_x += directions[direction][0]
            bullet_y += directions[direction][1]

            if bullet_x < 0 or bullet_x >= 5 or bullet_y < 0 or bullet_y >= 5:
                break

            elif territory[bullet_x][bullet_y] == "x":
                territory[bullet_x][bullet_y] = "."
                targets_hit.append(f"{[bullet_x, bullet_y]}")
                targets -= 1
                break
        if not targets:
            break


if targets:
    print(f"Training not completed! {targets} targets left.")
else:
    print(f"Training completed! All {len(targets_hit)} targets hit.")

print("\n".join(targets_hit))