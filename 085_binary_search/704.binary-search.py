#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums, target: int) -> int:
        first = 0
        last = len(nums)-1

        while first <= last:
            mid = (first + last) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1

        return -1
# @lc code=end

