n = int(input())
territory = []
teabags = 0
directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}
for r in range(n):
    row = input().split()
    territory.append(row)
    if "A" in row:
        x = r
        y = row.index("A")


while teabags < 10:
    territory[x][y] = "*"
    direction = input()
    x += directions[direction][0]
    y += directions[direction][1]
    if x >= n or y >= n or x < 0 or y < 0:
        break
    elif territory[x][y] == "R":
        territory[x][y] = "*"
        break
    elif territory[x][y] == "." or territory[x][y] == "*":
        territory[x][y] = "*"
    else:
        teabags += int(territory[x][y])
        territory[x][y] = "*"

if teabags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in territory:
    print(" ".join(row))