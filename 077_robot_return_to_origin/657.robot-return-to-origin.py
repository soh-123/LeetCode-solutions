#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        for move in moves:
            if move == 'R' :
                y+=1
            elif move == 'L':
                y-=1
            elif move == 'U':
                x+=1
            elif move == 'D':
                x-=1
        return x==0 and y==0
# @lc code=end

