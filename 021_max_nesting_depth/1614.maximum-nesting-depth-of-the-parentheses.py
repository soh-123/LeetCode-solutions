#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = [0]
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            depth.append(count)
        return max(depth)
# @lc code=end

