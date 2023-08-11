#
# @lc app=leetcode id= lang=python3
#
# [] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        sol = [[], []]

        for i in nums1:
            if i not in nums2:
                sol[0].append(i)

        for i in nums2:
            if i not in nums1:
                sol[1].append(i)

        return sol
# @lc code=end

