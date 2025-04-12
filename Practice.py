def wigglesort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    nums.sort()
    half = (n+1)//2
    small = nums[:half][::-1]
    large = nums[half:][::-1]
    for i in range(n):
        if i%2 == 0:
            nums[i] = small.pop(0)
        else:
            nums[i] = large.pop(0)