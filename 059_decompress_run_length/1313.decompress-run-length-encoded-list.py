#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums) :
        generated = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            generated += freq*[val]
        return generated



# @lc code=end

