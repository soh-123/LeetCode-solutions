#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr):
     
        rev = arr[::-1]
        max_num = -1
        for i in range(len(rev)):
            rev[i], max_num = max_num, max(max_num, rev[i])
        return rev[::-1]

# @lc code=end

