#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
class Solution:
    def finalPrices(self, prices):
        answer = []
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if prices[i] >= prices[j] and j>i:
                    answer.append(prices[i] - prices[j])
                    break
            else:
                answer.append(prices[i])
        return answer
# @lc code=end

