#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary) -> float:
        return (sum(salary) - max(salary) - min(salary))/(len(salary) - 2)
# @lc code=end

