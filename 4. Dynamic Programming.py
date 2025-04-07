class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i]: 以 nums[i] 结尾的最大子集长度
        prev = [-1] * n  # 用于追踪路径
        max_index = 0  # 最大子集的最后一个元素索引

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        # 回溯路径，构造结果
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = prev[max_index]

        return res[::-1]  # 结果从小到大


s = Solution()
print(s.largestDivisibleSubset([1, 2, 3]))  # 可能输出 [1, 2] 或 [1, 3]
print(s.largestDivisibleSubset([1, 2, 4, 8]))  # 输出 [1, 2, 4, 8]

from math import isqrt
def numSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 和为0时，需要0个平方数

    squares = [i*i for i in range(1, isqrt(n) + 1)]

    for i in range(1, n + 1):
        for sq in squares:
            if sq > i:
                break
            dp[i] = min(dp[i], dp[i - sq] + 1)

    return dp[n]

numSquares(12)
