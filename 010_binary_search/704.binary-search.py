#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums, target: int) -> int:
        try:
            index = nums.index(target)
            return index
        except ValueError:
            return -1
# @lc code=end

