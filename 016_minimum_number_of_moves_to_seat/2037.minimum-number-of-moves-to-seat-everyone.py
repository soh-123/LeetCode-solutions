#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        moves = 0
        for i, j in zip(sorted(seats), sorted(students)):
            moves += abs(j-i)
        return moves
# @lc code=end

