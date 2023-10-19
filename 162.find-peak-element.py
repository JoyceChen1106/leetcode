#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        index =0
        i=1

        if len(nums)== 1 :
            index=0

        elif len(nums)== 2:
            if nums[1]>nums[0]:
                index=1
            else:
                index=0

        for i in range(len(nums)-1):
            if nums[len(nums)-1] > nums[len(nums)-2] :
                index=len(nums)-1
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1] :
                index =i
        return(index)
        

# @lc code=end

