#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        - start by iterate until the smallest word. 
        - add the letters alternatively.
        - return the list with adding the remaining of either the two words.
        """
        sol = ""
        for i in range(min(len(word1), len(word2))):
            sol += word1[i] + word2[i]
        return sol + word1[i+1:] + word2[i+1:]
# @lc code=end
