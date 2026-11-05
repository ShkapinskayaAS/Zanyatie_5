n = int(input())

k = 0
total = 0

while total + (k + 1) <= n:
    k += 1
    total += k

print(k)
print(total)