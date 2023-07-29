#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] mat Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat) -> int:
        if len(mat) == 1: return mat[0][0]
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[len(mat)-1-i][i]

        if len(mat) % 2 != 0: 
            sum -= mat[len(mat)//2][len(mat)//2]

        return sum
    
# @lc code=end

