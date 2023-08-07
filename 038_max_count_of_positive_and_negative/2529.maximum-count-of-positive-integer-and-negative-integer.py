#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums) -> int:
        neg = 0
        pos = 0
        for i in nums:
            if i < 0:
                neg += 1
            elif i > 0:
                pos += 1
        return max(neg, pos)


# @lc code=end

