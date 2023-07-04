#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums, index):
        arr = []
        for n, i in zip(nums, index):
            arr.insert(i, n) 
        return arr
            
        
# @lc code=end

