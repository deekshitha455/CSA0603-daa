n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

print("Unique elements:", unique)