#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sol = ""
        for i in s.lower():
            if i.isalnum():
                sol += i
        
        if sol != sol[::-1]:
            return False
        else:
            return True

# @lc code=end

