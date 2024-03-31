#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict,l = {},[]

        #建立hashmap
        for i in nums :
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        freq_lst = list(my_dict.values())
        sorted_lst = sorted(freq_lst,reverse = True)
        idx = sorted_lst[k-1]

        #建立串列
        for i in  my_dict:
            if my_dict[i] >= idx:
                l.append (i)
                
            else:
                continue
        
        return l
            
        
        

        
# @lc code=end

