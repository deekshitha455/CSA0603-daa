n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

unique = list(set(arr))

print("Unique elements:", unique)