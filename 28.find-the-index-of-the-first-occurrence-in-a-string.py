#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1-l2+1):
            if haystack[i:i+l2] == needle:
                return i
        return -1
        
# @lc code=end

