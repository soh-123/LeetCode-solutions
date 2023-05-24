#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pS=0
        pT=0
        
        while pT<len(t) and pS<len(s) :
            if s[pS] == t[pT]:
                pS+=1
            pT+=1
			
        return pS==len(s)   
# @lc code=end

nums = "acb"
t = "ahbgdc"
sol = Solution()
single_num = sol.isSubsequence(nums, t)
print(single_num)
