#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights) -> int:
        expected = sorted(heights)
        indices = 0
        for i, j in zip(heights, expected):
            if i != j:
                indices +=1
        return indices
# @lc code=end

