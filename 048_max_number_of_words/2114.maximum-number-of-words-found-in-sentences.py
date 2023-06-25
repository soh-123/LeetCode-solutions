#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences) -> int:
        return max([len(i.split()) for i in sentences])
# @lc code=end

