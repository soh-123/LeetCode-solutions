#
# @lc app=leetcode id=2586 lang=python3
#
# [2586] Count the Number of Vowel Strings in Range
#

# @lc code=start
class Solution:
    def vowelStrings(self, words, left: int, right: int) -> int:
        vowels = "aeiou"
        count = 0
        for i in range(left, right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count+=1
      
        return count
# @lc code=end

