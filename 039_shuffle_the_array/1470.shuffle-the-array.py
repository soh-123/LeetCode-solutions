#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums, n: int):
        # sol = []
        # for i, j in zip(nums[:n], nums[n:]):
        #     sol += [i, j]
        # return sol
        return list(sum(zip(nums[:n], nums[n:]), ()))
# @lc code=end

