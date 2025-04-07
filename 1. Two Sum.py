''' 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''
def twoSum(self, nums, target):
    result = 0
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            result = nums[i]+nums[i+j+1]
            if result == target:
                return [i,i+j+1]

def twosum(nums,target):
    num_map = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in num_map:
            return [num_map[complement],index]
        num_map[number] = index
    return None

def twoSum(self, nums,target):
    num_dict = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement],i]
        num_dict[num]=i
    return []