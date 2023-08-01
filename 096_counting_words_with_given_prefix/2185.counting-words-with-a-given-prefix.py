#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
class Solution:
    def prefixCount(self, words, pref: str) -> int:
        return sum(1 for i in words if i.startswith(pref))
# @lc code=end

