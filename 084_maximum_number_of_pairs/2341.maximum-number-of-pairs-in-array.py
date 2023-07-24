#
# @lc app=leetcode id=2341 lang=python3
#
# [2341] Maximum Number of Pairs in Array
#

# @lc code=start
class Solution:
    def numberOfPairs(self, nums):
        singles = []
        pairs = 0
        for num in nums:
            if num in singles:
                pairs+=1
                singles.remove(num)
            else:
                singles.append(num)
        return [pairs , len(singles)]
        
# @lc code=end

