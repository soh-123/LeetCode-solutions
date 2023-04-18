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

# candies = [2,3,5,1,3]
# extraCandies = 3
# sol = Solution()
# single_num = sol.kidsWithCandies(candies, extraCandies)
# print(single_num)