#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRightDifference(self, nums):
        return [abs(sum(nums[:i + 1]) - sum(nums[i:])) for i in range(len(nums))]
# @lc code=end

