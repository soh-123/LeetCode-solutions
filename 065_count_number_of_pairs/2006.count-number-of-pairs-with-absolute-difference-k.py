#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
class Solution:
    def countKDifference(self, nums, k: int) -> int:
        #loop through the list twice, from back and front and check for the difference and count it if it's true
        count = 0
        for i in nums:
            for j in nums[::-1]:
                if j-i == abs(k):
                    count += 1
        return count

# @lc code=end

