#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        count = 0
        unique_list = set(nums)
        for i in nums:
            #I took this approach because num[j]=num[i]+diff and by replacing it in the other one it becomes num[k]=num[i]+2diff
            if i + diff in unique_list and i + diff * 2 in unique_list:
                count +=1
        return count
# @lc code=end

