#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums) -> int:
        # l1 = []
        # if nums != []:
        #     if len(nums) - len(set(nums)):

        # return len(nums) - len(set(nums))
        # uniqueList = []
        # duplicateList = []
 
        # for i in nums:
        #     if i not in uniqueList:
        #         uniqueList.append(i)
        #     elif i not in duplicateList:
        #         duplicateList.append(i)
        #         # print(duplicateList)
        #     return duplicateList[i]
        # return nums - set(nums)
        return 2*sum(set(nums)) - sum(nums)

# @lc code=end

# nums = [2,2,1]
# sol = Solution()
# single_num = sol.singleNumber(nums)
# print(single_num)
