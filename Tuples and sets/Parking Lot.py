parking = set()
for _ in range(int(input())):
    command = input().split(", ")
    direction = command[0]
    reg = command[1]
    if direction == "IN":
        parking.add(reg)
    else:
        parking.remove(reg)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
