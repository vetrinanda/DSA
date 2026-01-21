#How Many Numbers Are Smaller Than the Current Number

#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.
from ast import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        const=sorted(nums)
        d={}
        for i,num in enumerate(const):
            if num not in d:
                d[num]=i
        ret=[]
        for i in nums:
            ret.append(d[i])
        return ret
    
'''
nums =[8,1,2,2,3]
Output[4,0,1,1,3]
Expected[4,0,1,1,3]'''