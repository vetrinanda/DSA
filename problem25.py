'''69. Sqrt(x)
Easy
Topics
premium lock icon
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 '''
 
  
  
from ast import List
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            midsq = mid * mid

            if midsq == x:
                return mid
            elif midsq > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

        return ans
        