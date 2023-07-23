#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums, target: int):
        sol = []
        for i, a in enumerate(sorted(nums)):
            if a == target:
                sol.append(i)
        return sol


# @lc code=end

