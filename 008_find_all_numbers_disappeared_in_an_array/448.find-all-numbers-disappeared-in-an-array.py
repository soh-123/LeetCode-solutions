#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums):
        # nums.sort()
        # set(nums)
        new_list = [i for i in range(1,len(nums)+1)]
        return  list(set(new_list) - set(nums))

# @lc code=end

# nums = [1, 1]
# sol = Solution()
# single_num = sol.findDisappearedNumbers(nums)
# print(single_num)

