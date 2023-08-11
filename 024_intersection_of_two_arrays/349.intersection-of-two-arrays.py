#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        sol = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    sol.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    sol.append(i)
        return sol

# @lc code=end

