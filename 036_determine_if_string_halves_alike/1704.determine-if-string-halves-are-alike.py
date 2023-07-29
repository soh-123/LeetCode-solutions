#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        a = 0
        b = 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                a += 1
        for i in range(len(s)//2, len(s)):
            if s[i] in vowels:
                b += 1

        return a == b

                

# @lc code=end

