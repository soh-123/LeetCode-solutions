#
# @lc app=leetcode id=2119 lang=python3
#
# [2119] A Number After a Double Reversal
#

# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num%10 == 0 and num != 0:
            return False
        return True
    

# @lc code=end

