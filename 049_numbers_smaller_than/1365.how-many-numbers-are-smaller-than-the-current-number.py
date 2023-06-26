#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # arr = sorted(nums)
        # for i in range(len(nums)):
        #     nums[i] = arr.index(nums[i])
        return [sorted(nums).index(i) for i in nums]
# @lc code=end

