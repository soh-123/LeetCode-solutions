#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
       return "".join(word1) == "".join(word2)
        
    
        
# @lc code=end

