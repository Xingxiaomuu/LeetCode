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

# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/ 
class Solution(object):
    def containsDuplicate(self, nums):  
        num_dict={}
        for i,num in enumerate(nums):
            if num in num_dict:
                return True
            num_dict[num] = i
        return False   
    
# 219. Contains Duplicate II    
# https://leetcode.com/problems/contains-duplicate-ii/description/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_dict = {}
        n=len(nums)
        for i,num in enumerate(nums):
            if num in num_dict and (i-num_dict[num]<=k):
                return True
            num_dict[num] = i
        return False
    
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
    

def containsNearbyAlmostDuplicate(nums, k, t):
    if t < 0: return False # edge case 
    
    seen = {}
    for i, x in enumerate(nums): 
        bkt = x//(t+1)
        if bkt in seen and i - seen[bkt][0] <= k: 
            return True 
        if bkt-1 in seen and i - seen[bkt-1][0] <= k and abs(x - seen[bkt-1][1]) <= t: 
            return True 
        if bkt+1 in seen and i - seen[bkt+1][0] <= k and abs(x - seen[bkt+1][1]) <= t: 
            return True 
        seen[bkt] = (i, x) 
    return False 

containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) # False

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False # edge case 
        seen = {}
        for i,x in enumerate(nums):
            basket = x//(t+1)
            if basket in seen and i-seen[basket][0]<=k:
                return True
            if basket-1 in seen and i-seen[basket-1][0]<=k and abs(x-seen[basket-1][1])<=t:
                return True
            if basket+1 in seen and i-seen[basket+1][0]<=k and abs(x-seen[basket+1][1])<=t:
                return True
            seen[basket] = (i,x)
        return False

# 347. Top K Frequent Elements 
# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        freq = Counter(words)
        bucket = [[] for _ in range(len(words)+1)]
        for word, count in freq.items():
            bucket[count].append(word)
        result = []
        for i in range(len(words),0,-1):
            if len(result) >= k:
                break
            if bucket[i]:
                result.extend(sorted(bucket[i]))
        return result[:k]
    
# 274. H-Index
# https://leetcode.com/problems/h-index/description/
from collections import defaultdict
class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        bucket = [0] * (n+1)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1
        total= 0
        for i in range(n,-1,-1):
            total += bucket[i]
            if total >= i:
                return i
        return 0        

# 324. Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/description/   
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