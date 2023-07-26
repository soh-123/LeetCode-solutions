#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        return [candies[n] + extraCandies >= max(candies) for n in range(len(candies))] 
# @lc code=end

