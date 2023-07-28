#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#
import math
# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles) -> int:
        area_list = []
        for rec in rectangles:
            area_list.append(min(rec[0], rec[1]))
        return area_list.count(max(area_list))
# @lc code=end

