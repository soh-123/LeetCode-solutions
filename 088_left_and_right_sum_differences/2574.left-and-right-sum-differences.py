#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRightDifference(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return ans
# @lc code=end

