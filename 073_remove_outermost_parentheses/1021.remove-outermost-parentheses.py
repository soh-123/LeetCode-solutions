#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        sol = []
        cnt = 0
        for i in s:
            if i == "(" and cnt > 0: sol.append(i)
            if i == ")" and cnt > 1: sol.append(i)
            cnt += 1 if i == '(' else -1
        return "".join(sol)
# @lc code=end

