choco = list(map(int, input().split(", ")))
milk = list(map(int, input().split(", ")))
milkshakes = 0

while choco and milk:
    flag = False

    while milk[0] <= 0 or choco[-1] <= 0:     # deletes multiple neighboring zeroes or negatives
        if milk[0] <= 0:
            milk.pop(0)

        if choco[-1] <= 0:
            choco.pop(-1)

        if not milk:
            flag = True
            break
        if not choco:
            flag = True
            break

    if not choco:
        break
    if not milk:
        break

    if flag:    # breaks out of the for loop if milk or choco is empty
        break

    if choco[-1] == milk[0]:
        milkshakes += 1
        choco.pop(-1)
        milk.pop(0)
    else:
        milk.append(milk.pop(0))    # move the milk cup to the back
        choco[-1] -= 5  # decrease choco value by 5

    if milkshakes == 5:
        break   # break out of loop if enough milkshakes


if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

print(f"Chocolate: ", end="")
if choco:
    for ch in choco:
        if ch == choco[-1]:
            print(ch)
        else:
            print(ch, end=", ")
else:
    print("empty")
print(f"Milk: ", end="")
if milk:
    for m in milk:
        if m == milk[-1]:
            print(m)
        else:
            print(m, end=", ")
else:
    print("empty")
