#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
    def sortPeople(self, names, heights):
        zipped_pairs = zip(heights, names)
        z = [x for _, x in sorted(zipped_pairs)[::-1]]
        return z
# @lc code=end

