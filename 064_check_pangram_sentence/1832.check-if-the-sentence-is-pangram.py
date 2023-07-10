#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #1 line solution, finding wheater the sentence has all the alphabets or not
        return len(set(sentence)) >= 26
            
        
# @lc code=end

