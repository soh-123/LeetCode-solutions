#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#
import math
# @lc code=start
class Solution:
    def findGCD(self, nums) -> int:
        return math.gcd(min(nums), max(nums))
# @lc code=end

