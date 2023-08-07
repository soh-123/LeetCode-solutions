#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = s1[::-1]
        for i in range(0, len(s2)-1):
            if s2[i] == s1[0] and s2[i+1] == s1[1]:
                return True
        return False
# @lc code=end

