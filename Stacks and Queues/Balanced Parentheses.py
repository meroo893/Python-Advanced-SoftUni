text = input()
txt = []

for letter in text:
    txt.append(letter)

stack = []
opening = "([{"
parentheses = {
    "(": ")",
    "[": "]",
    "{": "}"
}
for letter in text:
    if letter in opening:
        stack.append(letter)
        txt.pop(0)
    elif stack:
        if txt.pop(0) == parentheses[stack[-1]]:
            stack.pop()
        else:
            break
if txt:
    print("NO")
else:
    print("YES")