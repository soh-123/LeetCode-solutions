#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums) -> int:
        """Check the count of each element, if it's equal 1 y3ny not repeated then add it to sum"""
        sum = 0
        for i in nums:
            if nums.count(i) == 1:
                sum += i
        return sum
# @lc code=end

