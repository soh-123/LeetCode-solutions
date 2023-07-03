#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        ans = sorted(str(num))
        return int(ans[0]+ans[2]) + int(ans[1]+ans[3])
# @lc code=end

