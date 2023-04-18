#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(min(len(word1),len(word2))):
    
            result += word1[i] + word2[i]
        return result + word1[i+1:] + word2[i+1:]
# @lc code=end

# word1 = "abc"
# word2 = "pqr"
# sol = Solution()
# single_num = sol.mergeAlternately(word1, word2)
# print(single_num)