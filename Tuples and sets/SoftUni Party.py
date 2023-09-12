invited = set()
for _ in range(int(input())):
    invited.add(input())

while True:
    guest = input()
    if guest == "END":
        break
    invited.remove(guest)

not_here = list(invited)
not_here.sort()
print(len(not_here))
for p in not_here:
    print(p)
