#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        # x = 0
        # for i in operations:
        #     if i == "++X" or i == "X++":
        #         x += 1
        #     elif i == "--X" or i == "X--":
        #         x -= 1
        # return x
        return sum(1 if '+' in o else -1 for o in operations)
# @lc code=end

