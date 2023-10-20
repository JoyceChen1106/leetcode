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
        for i in range(l1-l2+1): #兩兩字串相比並向後位移l1-l2+1步剛好到最後一個
            if haystack[i:i+l2] == needle: #如果內容相等則找到
                return i
        return -1
        
# @lc code=end

