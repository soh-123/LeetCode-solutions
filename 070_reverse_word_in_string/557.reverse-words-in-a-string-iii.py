#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = s.split()
        ans = []
        for word in sentence:
            ans.append(word[::-1])

        return " ".join(ans)
# @lc code=end

