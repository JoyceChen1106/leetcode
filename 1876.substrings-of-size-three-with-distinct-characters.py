#
# @lc app=leetcode id=1876 lang=python3
#
# [1876] Substrings of Size Three with Distinct Characters
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        k = 3
        n = len(s)
        count = 0

        while l < n-2 :

            while  r - l + 1 < k:
                r += 1
            if r - l + 1 == k:
                if s[l] != s[l+1] and s[l+1] != s[l+2] and s[l+2] != s[l]:
                    count += 1
            l += 1
            

        return count

            

        
# @lc code=end

