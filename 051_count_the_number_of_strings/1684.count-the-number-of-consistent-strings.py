#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        count = 0
        for word in words:
            if set(word) <= set(allowed):
                count += 1
        return count
# @lc code=end

