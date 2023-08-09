#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n * (n+1))//2
        left = 0
        for i in range(1, n+1):
            left += i
            if left == total:
                return i
            total -= i
        return -1


# @lc code=end

