#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        words_list = s[::-1].split()
        words_list.sort()
        ans = []
        for i in words_list:
            ans.append(i[1:][::-1])

        return ' '.join(ans)
# @lc code=end

