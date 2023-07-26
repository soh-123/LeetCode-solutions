#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return (n - 1 <= 0)
            else:
                return n == 0
        for index in range(len(flowerbed)):
            left = True
            right = True
            if flowerbed[index] == 0:
                if index == 0:
                    right = flowerbed[index + 1] == 0
                elif index == len(flowerbed) - 1:
                    left = flowerbed[index -1] == 0
                else:
                    right = flowerbed[index + 1] == 0
                    left = flowerbed[index -1] == 0
                if right and left:
                    flowerbed[index] = 1
                    n -= 1
                    if n == 0:
                        return True

        return n <= 0
# @lc code=end

