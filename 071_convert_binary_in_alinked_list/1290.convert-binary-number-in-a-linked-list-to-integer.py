#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        sol = 0
        while head:
            sol = sol *2 +head.val
            head = head.next
        return sol

    
# @lc code=end

