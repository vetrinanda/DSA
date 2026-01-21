#Two Sum

'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


from ast import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i
            
            
# nums =[2,7,11,15]
# target =9
# sol=Solution()
# print(sol.twoSum(nums,target))
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].