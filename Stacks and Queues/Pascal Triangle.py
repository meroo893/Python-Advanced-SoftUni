def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    return n*factorial(n-1)


row = int(input())
coefficients = []
for k in range(row+1):
    coef = factorial(row)/(factorial(k)*factorial(row-k))
    coefficients.append(int(coef))

for c in coefficients:
    print(c, end=" ")