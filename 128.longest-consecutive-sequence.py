#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
 
        num_set = set(nums)
        max_length = 0
        
        for num in nums :
            #找起始點
            if  num-1 not in num_set:
                length = 0
                while  (num+length) in num_set :
                    length += 1
                max_length = max(length,max_length)
        
        
        return max_length
# @lc code=end

