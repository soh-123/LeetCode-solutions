#
# @lc app=leetcode id= lang=python3
#
# [] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain) -> int:
        current = 0
        highest = 0
        for i in gain:
            current += i
            highest = max(current, highest)
        return highest
# @lc code=end

