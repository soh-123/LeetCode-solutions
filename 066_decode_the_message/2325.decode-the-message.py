#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        sol = ''
        j = 0
        mapping = {' ': ' '}
        letter = "abcdefghijklmnopqrstuvwxyz"

        for i in key:
            if i not in mapping:
                mapping[i] = letter[j]
                j+=1

        
        for i in message:
            sol += mapping[i]

        return sol

# @lc code=end

