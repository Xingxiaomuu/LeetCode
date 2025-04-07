def topKfrequent(nums,k):
    from collections import defaultdict
    freq = defaultdict(int)
    for num in nums:
        freq[num]+=1
    bucket = [[] for _ in range(len(nums)+1)]
    for num,freq in freq.items():
        bucket[freq].append(num)
    result = []
    for i in range(len(nums),0,-1):
        if len(result)>=k:
            break
        if bucket[i]:
            result.extend(bucket[i])
    return result[:k]
# print(topKfrequent([1,1,1,2,2,3],2))
# pytest -vv Test-pytest.py
def test_topKfrequent():
    assert topKfrequent([1,1,1,2,2,3],2) == [1,2]
    assert topKfrequent([1],1) == [1]
    assert topKfrequent([1,2],2) == [1,2]
    assert topKfrequent([3,0,1,0],1) == [0]
    assert topKfrequent([4,4,4,4],1) == [4]
    assert topKfrequent([1,2,3,4,5],3) == [1,2,3]