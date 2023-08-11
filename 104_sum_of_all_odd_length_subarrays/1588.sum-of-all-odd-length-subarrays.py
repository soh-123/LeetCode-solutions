#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        if len(arr) <= 2:
            return sum(arr)  
              
        if len(arr)%2 == 1: # if length odd
            res = 2*sum(arr) #count ones and count the large odd
        else: # if length even
            res = sum(arr) 

        for i in range(3, len(arr), 2):   # for each window size        
            for j in range(0,len(arr)-i+1): # sum elements 
                res += sum(arr[j:j+i])  
        return res

# @lc code=end

