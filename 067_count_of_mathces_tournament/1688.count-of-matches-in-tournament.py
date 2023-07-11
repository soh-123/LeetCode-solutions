#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        #first solution: follow the problem sequence 
        # matches = 0
        
        # while n != 1:
        #     if n%2 == 0:
        #         matches += n/2
        #         n = n/2
        #     else:
        #         matches += (n - 1) / 2
        #         n = (n - 1) / 2 + 1

        # return int(matches)
    
        #second solution: logically number of losing teams is all the teams minus 1 because only one will win
        return n-1

# @lc code=end

