#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices) -> str:
        ans = [''] * len(s)
        for index, letter in enumerate(s):
            ans[indices[index]] = letter
        return "".join(ans)
# @lc code=end

