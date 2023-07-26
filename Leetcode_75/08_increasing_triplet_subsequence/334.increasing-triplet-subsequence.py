#
# @lc app=leetcode id= lang=python3
#
# [] Increasing Triplet Subsequence
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
