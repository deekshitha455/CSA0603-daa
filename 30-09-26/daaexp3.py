n = int(input("Enter size: "))
a = list(map(int, input("Enter elements: ").split()))

total = 0

for i in range(n):
    s = set()

    for j in range(i, n):
        s.add(a[j])

        sum1 = 0

        for x in s:
            sum1 += x * x

        total += sum1

print("Total Sum:", total)
