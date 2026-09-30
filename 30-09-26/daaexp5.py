n = int(input("Enter size: "))
a = list(map(int, input("Enter elements: ").split()))

maximum = a[0]

for x in a:
    if x > maximum:
        maximum = x

print("Maximum Element:", maximum)
