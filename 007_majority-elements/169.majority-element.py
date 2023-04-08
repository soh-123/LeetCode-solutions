#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# @lc code=start
class Solution:
    def majorityElement(self, nums:list) -> int:
        return max(set(nums), s = nums.count)

              
# @lc code=end

# nums = [2,2,1,1,1,2,2]
# sol = Solution()
# single_num = sol.majorityElement(nums)
# print(single_num)

