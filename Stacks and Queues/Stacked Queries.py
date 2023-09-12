stack = []

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        if stack:
            print(max(stack))
    else:
        if stack:
            print(min(stack))

while stack:
    if len(stack) > 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())
