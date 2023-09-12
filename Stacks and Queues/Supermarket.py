q = []

while True:
    command = input()
    if command == "End":
        break
    elif command == "Paid":
        while q:
            print(q.pop(0))
    else:
        q.append(command)

print(f"{len(q)} people remaining.")
