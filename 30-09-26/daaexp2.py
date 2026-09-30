n = int(input("Enter size of first array: "))
a = list(map(int, input("Enter elements: ").split()))

m = int(input("Enter size of second array: "))
b = list(map(int, input("Enter elements: ").split()))

print("Common Elements:")

for x in a:
    if x in b:
        print(x, end=" ")
