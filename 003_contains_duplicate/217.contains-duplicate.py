#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums) -> bool:
        unique_list = set(nums)
        return len(unique_list) != len(nums)
            

# @lc code=end


