#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        result = []
        nums.sort()
        for first in range(len(nums) - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, len(nums) - 1
            while second < third:
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue
                total = nums[first] + nums[second] + nums[third]
                if total == 0:
                    result.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                elif total < 0:
                    second += 1
                else:
                    third -= 1
        return result
 
        
# @lc code=end

