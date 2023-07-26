#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        - checking if we found the letter in the word:
        - if we found it;
        - get all the letters before it + ch and reverse it, in the same step add the rest of the word.
        - if we didn't return the word as it is.
        """
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i+1][::-1] + word[i+1:]
        return word


                
# @lc code=end

