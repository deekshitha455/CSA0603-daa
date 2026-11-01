n = 4

a = 1
b = 1

for i in range(2, n + 1):
    c = a + b
    a = b
    b = c

print(b)