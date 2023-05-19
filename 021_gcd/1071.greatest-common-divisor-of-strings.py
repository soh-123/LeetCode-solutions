#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
import math
# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if ( str1 + str2 ) != ( str2 + str1 ):		
            return ''
			
        elif str1 == str2:		
            return str1
        
        else:
            length_by_gcd = math.gcd( len(str1), len(str2) )
            return str1[:length_by_gcd]
        
# @lc code=end

