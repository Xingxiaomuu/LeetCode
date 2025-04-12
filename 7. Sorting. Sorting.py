from collections import Counter
def frequencySort(nums):
    freq = Counter(nums)
    nums.sort(key=lambda x: (freq[x],-x))
    return nums

print(frequencySort([1,1,1,2,2,3]))
a = sorted([1,1,1,2,2,3], key = lambda x:(Counter([1,1,1,2,2,3])[x],-x))
print(a)