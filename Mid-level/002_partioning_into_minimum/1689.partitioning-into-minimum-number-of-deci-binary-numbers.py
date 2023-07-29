#
# @lc app=leetcode id= lang=python3
#
# [] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(i) for i in n)
# @lc code=end

