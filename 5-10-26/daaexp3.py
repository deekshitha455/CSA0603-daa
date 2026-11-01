n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

x = int(input("Enter element to search: "))
low = 0
high = n - 1
found = False
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
if found:
    print("Element found")
else:
    print("Element not found")

