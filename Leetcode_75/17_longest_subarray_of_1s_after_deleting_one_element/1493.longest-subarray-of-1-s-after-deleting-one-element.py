#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums) -> int:
        max_cons = 0
        ones = 0
        zeroes = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
                while zeroes > 1:
                    if nums[left] == 0:
                        zeroes -= 1
                    else:
                        ones -= 1
                    left += 1
            else:
                ones += 1

            max_cons = max(max_cons, ones)

        return max_cons if zeroes == 1 else max_cons - 1
# @lc code=end

