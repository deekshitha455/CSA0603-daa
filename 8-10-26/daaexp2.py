def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def maximum(arr):
        prev = 0
        curr = 0

        for x in arr:
            temp = max(curr, prev + x)
            prev = curr
            curr = temp

        return curr

    return max(maximum(nums[:-1]), maximum(nums[1:]))

nums = [1, 2, 3, 1]

print(rob(nums))