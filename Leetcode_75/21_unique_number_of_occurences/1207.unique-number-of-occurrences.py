#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from collections import Counter
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        occ = Counter(arr)
        return len(occ) == len(set(occ.values()))
        
# @lc code=end

