def heapify(nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Check left child
    if left < n and nums[left] > nums[largest]:
        largest = left
    # Check right child
    if right < n and nums[right] > nums[largest]:
        largest = right
    # If largest is not the root
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]

        # Heapify the affected subtree
        heapify(nums, n, largest)
def heap_sort(nums):
    n = len(nums)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums
# Input
n = int(input("Enter number of elements: "))
nums = []
for i in range(n):
    nums.append(int(input("Enter element: ")))
# Sort
heap_sort(nums)
print("Sorted array:", nums)

