#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        isVowel = [c in "aeiou"for c in s]
        maxVowel = countVowel = sum(isVowel[:k])

        for i in range(k, len(s)):
            if isVowel[i-k]:
                countVowel -= 1
            if isVowel[i]:
                countVowel += 1
            maxVowel = max(maxVowel, countVowel)
        return maxVowel

# @lc code=end

