#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = len(nums)
        for n in nums:
            if n == 0:
                nums.remove(0)
                nums.insert(x-1, 0)
            elif 0 not in nums:
                return

        return nums
        
# @lc code=end

# nums = [0,1,0,3,12]
# sol = Solution()
# single_num = sol.moveZeroes(nums)
# print(single_num)