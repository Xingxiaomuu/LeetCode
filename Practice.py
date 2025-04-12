def hIndex(citations):
    n=len(citations)
    bucket = [0]*(n+1)
    for c in citations:
        if c >= n:
            bucket[n] += 1
        else:
            bucket[c] += 1
    total = 0
    for i in range(n, -1, -1):
        total += bucket[i]
        if total >= i:
            return i
    return 0

citations = [3,0,6,1,5]
print(hIndex(citations))