#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

class Solution:
    def maxProfit(self, prices) -> int:
        buy = prices[0]
        sell = 0

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sell = max(sell, prices[i]-buy)
        return sell
        

# @lc code=end


# var = Solution()
# profit = var.maxProfit([7,5,3,6,4,1])
# print(profit)

