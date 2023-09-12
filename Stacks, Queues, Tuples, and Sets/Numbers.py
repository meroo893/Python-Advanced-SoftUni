first = set(input().split())
second = set(input().split())

for _ in range(int(input())):
    command = input().split()
    if command[0] == "Add":
        command.remove("Add")
        if command[0] == "First":
            command.remove("First")
            for num in command:
                first.add(num)
        else:
            command.remove("Second")
            for num in command:
                second.add(num)

    elif command[0] == "Remove":
        command.remove("Remove")
        if command[0] == "First":
            command.remove("First")
            for num in command:
                if num in first:
                    first.remove(num)
        else:
            command.remove("Second")
            for num in command:
                if num in second:
                    second.remove(num)
    else:
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")


first = list(map(int, first))
second = list(map(int, second))
first.sort()
second.sort()

if not first:
    print("")
else:
    for n in first:
        if n == first[-1]:
            print(n)
        else:
            print(n, end=", ")
if not second:
    print("")
else:
    for n in second:
        if n == second[-1]:
            print(n)
        else:
            print(n, end=", ")