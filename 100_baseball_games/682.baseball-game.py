#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations) -> int:
        new_record = []
        for i in operations:
            if i == "C":
                new_record.pop()
            elif i == "D":
                new_record.append(new_record[-1]*2)
            elif i == "+":
                new_record.append(new_record[-1]+new_record[-2])
            elif i == "x":
                new_record.clear()
            else:
                new_record.append(int(i))
        return sum(new_record)
# @lc code=end

