#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
# @lc code=end

nums = [0,1,2,4,5,7]
sol = Solution()
single_num = sol.summaryRanges(nums)
print(single_num)