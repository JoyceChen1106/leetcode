#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newS = "".join(char for char in s if char.isalnum())
        if newS == newS[::-1]:
            return True
        return False

# @lc code=end

