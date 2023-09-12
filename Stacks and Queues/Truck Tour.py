from collections import deque
indexes = []
n = int(input())
stations = []
for _ in range(n):
    info = tuple(map(int, input().split()))
    stations.append(info)
stations = deque(stations)

for i in range(len(stations)):
    circle = True
    distance = 0
    fuel = 0
    for station in stations:
        distance += station[1]
        fuel += station[0]
        if distance > fuel:
            circle = False
            break
    if circle:
        indexes.append(i)
    stations.append(stations.popleft())

print(min(indexes))