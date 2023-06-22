#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#
import math
# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numbers = list(map(int, str(n)))
        return math.prod(numbers) - sum(numbers)
# @lc code=end

