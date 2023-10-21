#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        left = 0
        right = len(people)-1

        people.sort(reverse=True)  #由大到小排序

        while left<=right :
            if people[left] == limit :
                count += 1 
                left += 1
            elif people[left]+people[right] <= limit :
                count += 1
                left += 1
                right -=1
            else:
                count += 1
                left += 1
        return count
        
# @lc code=end

