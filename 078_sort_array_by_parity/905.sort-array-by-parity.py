#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums) :
        even = []
        odd = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd
# @lc code=end

