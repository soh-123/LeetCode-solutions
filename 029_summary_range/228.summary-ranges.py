#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums):
        ranges = []
        i =0
        while i < len(nums):
            start = nums[i]
            while i < len(nums)-1 and nums[i] == nums[i + 1] - 1:
                i+=1
            end = nums[i]
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(end))
            i += 1
        return ranges
# @lc code=end

