cmd = input().split()
n = int(cmd[0])
m = int(cmd[1])
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

conjunction = n_set & m_set
for item in conjunction: print(item)