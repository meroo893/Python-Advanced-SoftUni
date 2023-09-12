food = int(input())

orders = list(map(int, input().split()))
print(max(orders))
while orders and food >= orders[0]:
    food -= orders.pop(0)

if not orders:
    print("Orders complete")
else:
    orders = list(map(str, orders))
    print(f"Orders left: {' '.join(orders)}")