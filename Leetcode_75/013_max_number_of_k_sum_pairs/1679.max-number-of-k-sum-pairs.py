#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-k Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums, k) -> int:
        left = 0
        right = len(nums)-1
        nums.sort()
        count = 0
        while left < right:
            if nums[left]+nums[right] == k and left < right:
                count += 1
                left+=1
                right-=1
            elif nums[left] + nums[right] > k:
                right-=1
            else:
                left+=1
        return count
# @lc code=end

