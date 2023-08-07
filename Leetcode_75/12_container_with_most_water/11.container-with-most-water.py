#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height) -> int:
        """
        Two pointers from both sides
        """
        sol = 0
        left = 0
        right = len(height)-1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            sol = max(sol, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return sol
# @lc code=end

