'''Contains A Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.
'''

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets=set(nums)
        if len(sets)==len(nums):
            return False
        else:
            return True