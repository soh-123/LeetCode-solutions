#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum/k
        


# @lc code=end

