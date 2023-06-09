#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
import numpy as np
# @lc code=start
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        product = 1
        
        #multiply from left
        for i, num in enumerate(nums):
            result[i] *= product
            product *= num

        product = 1   #reset
        #multiply from right
        for i in range(n - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result


# @lc code=end

nums = [1,2,3,4]
sol = Solution()
single_num = sol.productExceptSelf(nums)
print(single_num)