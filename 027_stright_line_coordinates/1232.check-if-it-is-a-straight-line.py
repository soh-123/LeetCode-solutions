#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) < 3:
            return True
        
        (x1, y1) = coordinates[0]
        (x2, y2) = coordinates[1]

        for i, j in coordinates:
            if (x2 - x1)*(j - y1) != (i - x1)*(y2 - y1):
                return False

        return True
# @lc code=end

nums = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
sol = Solution()
single_num = sol.checkStraightLine(nums)
print(single_num)