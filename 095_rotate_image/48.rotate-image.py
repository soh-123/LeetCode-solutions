#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
# @lc code=end

