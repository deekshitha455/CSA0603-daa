n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter sorted elements: ").split()))
x = int(input("Enter number to search: "))

left = 0
right = n - 1

while left <= right:
    mid = left + (right - left) // 2

    if arr[mid] == x:
        print("Element found at index", mid)
        break
    elif arr[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")