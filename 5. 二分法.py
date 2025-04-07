def search(nums, target):
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
'''
nums = [-1,0,3,5,9,12]
target = 9
result = search(nums,target)
print(result)'''

def isBadVersion():
    pass
def firstBadVersion(self, n):
    left,right=1,n
    while left<=right:
        mid = (left+right)//2
        if isBadVersion(mid):
            right = mid - 1
            if not isBadVersion(right):
                return mid
        else:
            left = mid + 1
            if isBadVersion(left):
                return left
    return -1
    

def searchInsert(self, nums, target):
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right=mid-1
    return left

def findMin(nums):
    left,right=0,len(nums)-1
    while left<right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


def search(self, nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # 左半段有序
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 右半段有序
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1            
    return -1

def findPeakElement(nums):
    left,right = 0,len(nums)-1
    
    while left < right:
        mid = (left+right)//2
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid]<nums[mid+1]:
            left = mid+1
        else:
            right=mid-1
    return -1

findPeakElement([1,2,3,1])
findPeakElement([1,2,1,3,5,6,4])