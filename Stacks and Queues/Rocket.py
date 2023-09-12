n = int(input())
columns = n+5
for i in range(columns):
    if i == columns//2:
        print("^", end="")
    else:
        print("_", end="")
print()
for i in range(columns-4):
    if i == (columns-4)//2:
        print(r"_/|\_", end="")
    else:
        print("_", end="")
print()
for i in range(columns-6):
    if i == (columns-6)//2:
        print(r"_/|||\_", end="")
    else:
        print("_", end="")
print()


thinning = ""
for i in range(int(n/2)):
    und_len = int((columns - i*2 - 5)/2)-1
    for _ in range(und_len):
        if i == (n/2) - 2:
            thinning += "_"
        print("_", end="")
    print("/", end="")
    if i == (n / 2) - 2:
        thinning += "/"
    for _ in range(int(n/2)-und_len):
        if i == (n/2) - 2:
            thinning += "."
        print(".", end="")
    print("|||", end="")
    if i == (n / 2) - 2:
        thinning += "|||"
    for _ in range(int(n/2)-und_len):
        if i == (n/2) - 2:
            thinning += "."
        print(".", end="")
    print('\\', end="")
    if i == (n / 2) - 2:
        thinning += "\\"
    for _ in range(und_len):
        if i == (n/2) - 2:
            thinning += "_"
        print("_", end="")
    print()
print(thinning)


for _ in range(n):
    for i in range(columns-2):
        if i == (columns-2)//2:
            print("|||", end="")
        else:
            print("_", end="")
    print()
for i in range(columns - 2):
    if i == (columns - 2) // 2:
        print("~~~", end="")
    else:
        print("_", end="")
print()


for i in range(int(n/2)):
    und_len = int((columns-5-i*2)/2)
    for _ in range(und_len):
        print("_", end="")
    print("//", end="")
    for _ in range(i):
        print(".", end="")
    print("!", end="")
    for _ in range(i):
        print(".", end="")
    print("\\\\", end="")
    for _ in range(und_len):
        print("_", end="")
    print()