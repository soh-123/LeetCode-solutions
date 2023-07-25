#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sol = []
        for i in s:
            sol.append(s.count(i))
        if len(set(sol)) != 1:
            return False
        return True
            
        
# @lc code=end

