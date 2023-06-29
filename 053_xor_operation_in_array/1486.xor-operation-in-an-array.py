#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0

        for i in range(n):
            ans ^= (start + 2 * i)
        return ans
# @lc code=end

