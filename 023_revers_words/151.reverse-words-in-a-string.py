#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ".join(s.split()[::-1]))

# @lc code=end
nums = "the sky is blue"
sol = Solution()
single_num = sol.reverseWords(nums)
print(single_num)
