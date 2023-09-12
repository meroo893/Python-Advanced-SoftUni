from collections import deque

text = deque(input().split())
mains = ["red", "yellow", "blue"]
secondary = {"orange": ["red", "yellow"],
            "purple": ["red", "blue"],
            "green": ["yellow", "blue"]}
colors = []
while text:
    right = text.pop()
    if text:
        left = text.popleft()
    else:
        left = ""
    if left+right in mains or left+right in secondary:
        colors.append(left+right)
    elif right + left in mains or right + left in secondary:
        colors.append(right+left)
    else:
        right = right[:-1]
        left = left[:-1]
        middle = int(len(text)/2)
        if right:
            text.insert(middle, right)
        if left:
            text.insert(middle, left)   # MIGHT BE VICE VERSA IDK

for color in colors:
    if color in secondary.keys() and (secondary[color][0] not in colors or secondary[color][1] not in colors):
        colors.remove(color)

print(colors)