#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
# @lc code=end

