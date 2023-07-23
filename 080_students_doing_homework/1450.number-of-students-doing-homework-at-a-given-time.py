#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        count = 0

        for i, j in zip(startTime, endTime):
            if i <= queryTime <= j:
                count +=1
        return count
# @lc code=end

