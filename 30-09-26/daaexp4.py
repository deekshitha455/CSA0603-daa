n = int(input("Enter size: "))
a = list(map(int, input("Enter elements: ").split()))

k = int(input("Enter k: "))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j] and (i * j) % k == 0:
            count += 1

print("Number of Pairs:", count)
