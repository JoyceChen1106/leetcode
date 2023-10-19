#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def find_square_sum(nums:int) -> int:
            _curr_sum= 0
            while nums>0 :
                digit = nums %10
                _curr_sum += digit **2  #2平方語法
                nums //= 10
            return _curr_sum
        
        slow = fast =n

        while True:
            slow = find_square_sum(slow)
            fast = find_square_sum(find_square_sum(fast))

            if slow==fast:
                break
        
        return slow ==1
    



        
# @lc code=end

