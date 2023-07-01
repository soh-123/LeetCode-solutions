#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded, first: int):
        new_encoded = []
        new_encoded.append(first)
        for i in range(len(encoded)):
            new_encoded.append(new_encoded[i] ^ encoded[i])
        return new_encoded
# @lc code=end

