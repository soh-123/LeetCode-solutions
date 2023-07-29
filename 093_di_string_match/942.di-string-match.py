#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#

# @lc code=start
class Solution:
    def diStringMatch(self, s: str):
        a = 0
        b = len(s)
        sol = []

        for i in range(b):
            if s[i] == "D":
                sol.append(b)
                b -= 1
            else:
                sol.append(a)
                a += 1
        
        if s[len(s) - 1] == "I":
            sol.append(a)
        else:
            sol.append(b)
        return sol

# @lc code=end

