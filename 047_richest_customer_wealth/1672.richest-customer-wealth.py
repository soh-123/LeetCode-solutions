#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts) -> int:
        return max([sum(i) for i in accounts])
# @lc code=end

