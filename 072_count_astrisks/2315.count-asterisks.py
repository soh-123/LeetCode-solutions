#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        sol = ''
        for i  in range(0, len(s), 2):
            sol += s[i]
        return sol.count("*")
# @lc code=end

