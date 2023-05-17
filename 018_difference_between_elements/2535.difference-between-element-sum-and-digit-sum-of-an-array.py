#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums):
        s = sum(nums)
        res = []
        for n in nums:
            dig = 0
            for digit in str(n):
                dig += int(digit)
            res.append(dig)
            
        return abs(s - sum(res))
# @lc code=end

# nums = [1,15,6,3]
# sol = Solution()
# single_num = sol.differenceOfSum(nums)
# print(single_num)