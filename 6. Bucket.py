from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        # 1. 统计每个元素的频率
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # 2. 创建频率桶，桶的下标表示频率
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]  # 频率从 1 到 n，所以需要 n+1 个桶
        
        # 3. 将元素放入对应频率的桶中
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # 4. 从频率最高的桶开始，取出前 k 个频率最高的元素
        result = []
        for i in range(n, 0, -1):  # 从最大频率开始遍历
            if buckets[i]:
                result.extend(buckets[i])
            if len(result) >= k:  # 一旦取到 k 个元素就可以停止
                break
        
        return result[:k]  # 返回前 k 个元素

# 测试
nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))  # 输出 [1, 2]


class Solution(object):
    def frequencySort(self, s):
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        n = len(s)
        bucket = [[] for _ in range(n+1)]
        for char,freq in char_dict.items():
            bucket[freq].append(char)
        result = []
        for i in range(n,0,-1):
            for char in bucket[i]:
                result.append(char * i)
        return ''.join(result)


class Solution(object):
    def maximumGap(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        distance = 0
        for i in range(1,n):
            distance = max(distance, (nums[i]-nums[i-1]))
        return distance
    
#220. Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/description/
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        length = len(nums)
        for i in range(length):
            for j in range(i+1,min(i+indexDiff+1,length)):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False