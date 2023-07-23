#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums) -> int:
        ans = []
        for i in nums:
            if i in ans:
                return i
            else:
                ans.append(i)

# @lc code=end

