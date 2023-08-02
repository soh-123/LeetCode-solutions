#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#
import itertools
# @lc code=start
class Solution:
    def countNegatives(self, grid) -> int:
        
        count = 0
        for i in list(itertools.chain.from_iterable(grid)):
            if i < 0:
                count += 1
        return count
                
# @lc code=end

