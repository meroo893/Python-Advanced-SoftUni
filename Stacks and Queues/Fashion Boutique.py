clothes = list(map(int, input().split()))

rack = int(input())
racks_needed = 0
on_rack = 0
while clothes:
    if on_rack + clothes[0] > rack:
        racks_needed += 1
        on_rack = 0
    elif on_rack + clothes[0] == rack:
        racks_needed += 1
        on_rack = 0
        clothes.pop(0)
    else:
        on_rack += clothes.pop(0)

if on_rack:
    racks_needed += 1
print(racks_needed)