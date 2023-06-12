#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters, target: str):
        if letters[0] > target:
            return letters[0]
        
        l = 0
        h = len(letters)
        while l < h:
            mid = l + (h - l) // 2
            if letters[mid] > target:
                h = mid
            else:
                l = mid + 1
        return letters[l % len(letters)]
                
# @lc code=end

