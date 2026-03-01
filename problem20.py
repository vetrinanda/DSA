'''
Given an integer array nums, return the k largest elements in the array in any order.
This code can have yrt another solution also'''
from ast import List
import heapq
nums =[3,2,1,5,6,4]
k=2
heapq.heapify(nums)
print(nums)

def sortedSquares(self, nums: List[int]) -> List[int]: 
    l = 0
    r = len(nums) - 1
    result = []
    
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            result.append(nums[l] ** 2)
            l += 1
        else:
            result.append(nums[r] ** 2)
            r -= 1
    
    return result[::-1]