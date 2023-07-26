#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution:
    def separateDigits(self, nums):
        lis = []
        for i in nums:
            for j in str(i):
                lis.append(int(j))
        return lis
# @lc code=end

