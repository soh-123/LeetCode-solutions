#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        # return x == x[::-1]
        if x == x[::-1]:
            return True



# @lc code=end

