'''
Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
'''

from ast import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret=[]
        while matrix:
            ret+=(matrix.pop(0))

            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            if matrix:
                ret+=(matrix.pop()[::-1])

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))


        return ret

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# sol=Solution()    
# print(sol.spiralOrder(matrix))
# Output: [1,2,3,6,9,8,7,4,5]
# Explanation: The spiral order of the matrix is as follows:
# 1 → 2 → 3
#           ↓
# 4 → 5 → 6
#           ↓
# 7 → 8 → 9