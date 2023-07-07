#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        res=0
        rule={"type":0,"color":1,"name":2}
        for i in items:
            if i[rule[ruleKey]]==ruleValue:
                res+=1
        return res
        
# @lc code=end

