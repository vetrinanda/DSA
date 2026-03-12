'''2. Add Two Numbers
Attempted
Medium
Topics
premium lock icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 '''
 
 
#  Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from problem18 import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_values=[]
        l2_values=[]
        curr=l1

        while curr:
            l1_values.append(str(curr.val))
            curr=curr.next
        
        curr = l2                          # fix 1: traverse l2
        while curr:
            l2_values.append(str(curr.val))
            curr = curr.next

        l1_values=l1_values[::-1]
        l2_values=l2_values[::-1]

        l1_num=int(''.join(l1_values))
        l2_num=int(''.join(l2_values))

        new_digits=str(l1_num+l2_num)[::-1]
        dummy=ListNode()
        curr=dummy

        for d in new_digits:
            curr.next=ListNode(int(d))
            curr=curr.next
        return dummy.next
