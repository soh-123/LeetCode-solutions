#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums):
        total =0
        new_list = []
        for n in nums:
            total += n
            new_list.append(total)
        return new_list
# @lc code=end

