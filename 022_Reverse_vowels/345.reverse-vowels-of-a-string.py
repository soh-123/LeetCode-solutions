#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
import random
# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_vowls = [vowl for vowl in s if vowl in 'aeiouAEIOU']
        j=len(s_vowls)-1
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in 'aeiouAEIOU':
                s_list[i] = s_vowls[j]
                j -= 1
        return ''.join(s_list)
        
# @lc code=end
nums = "hello"
sol = Solution()
single_num = sol.reverseVowels(nums)
print(single_num)
