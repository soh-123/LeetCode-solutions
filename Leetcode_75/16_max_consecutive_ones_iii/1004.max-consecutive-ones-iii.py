#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        """
        Check for max number of 1's after flipping k number of 0's
        """
        l = max_cons = 0

        for r, num in enumerate(nums):
            k -= 1 - num

            if k < 0:
                k += 1-nums[l]
                l += 1
            else:
                max_cons = max(max_cons, r - l + 1)
        return max_cons
# @lc code=end

