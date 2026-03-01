'''238. Product of Array Except Self
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0] This code can have yrt another solution also '''

from ast import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=1
        r=1
        n=len(nums)
        l_arr=[0]*n
        r_arr=[0]*n

        for i in range(n):
            j=-i-1
            l_arr[i]=l
            r_arr[j]=r
            l*=nums[i]
            r*=nums[j]

        return [l_r*r_r for l_r,r_r in zip(l_arr,r_arr)]