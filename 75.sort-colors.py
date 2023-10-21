#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #使用bubble sort
        n = len(nums)
        
        while (n>0):
            n -= 1
            for i in range(len(nums)-1):
                if nums[i] >  nums[i+1]:
                    temp = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temp

# @lc code=end

