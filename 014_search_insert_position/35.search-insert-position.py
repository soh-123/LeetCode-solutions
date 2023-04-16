#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        
        return len(nums)
# @lc code=end

nums = [1,3,5,6]
target = 2
sol = Solution()
single_num = sol.searchInsert(nums, target)
print(single_num)