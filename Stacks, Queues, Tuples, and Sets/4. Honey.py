from collections import deque

bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = deque(input().split())
honey = 0
while bees and nectar:
    matched_bee = bees.popleft()
    matched_nectar = nectar.pop()
    if matched_bee <= matched_nectar:
        honey += abs(eval(f"{matched_bee} {symbols.popleft()} {matched_nectar}"))
    else:
        bees.appendleft(matched_bee)

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")