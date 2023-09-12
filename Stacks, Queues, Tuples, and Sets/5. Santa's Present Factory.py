from collections import deque

presents = {}
magic_cost = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
gifts = ["Doll", "Teddy bear", "Wooden train", "Bicycle"]
gifts.sort()

for gift in gifts:
    presents[gift] = 0

materials = deque(map(int, input().split()))
magics = deque(map(int, input().split()))

while magics and materials:
    material = materials.pop()
    magic = magics.popleft()
    prod = magic * material
    if prod < 0:
        materials.append(magic + material)
    elif prod == 0:
        if magic != 0:
            magics.appendleft(magic)
        elif material != 0:
            materials.append(material)
    else:
        if magic_cost.get(prod):
            presents[magic_cost.get(prod)] += 1
        else:
            material += 15
            materials.append(material)

if (presents["Bicycle"] and presents["Teddy bear"]) or (presents["Wooden train"] and presents["Doll"]):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

for toy, amount in presents.items():
    if amount > 0:
        print(f"{toy}: {amount}")
