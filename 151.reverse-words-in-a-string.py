#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_list = s.split(" ")#以空格作為區分，將字串切開來存成一個list   e.g['a', 'good', '', '', 'example']

        reverse = reversed(s_list)  # 反轉串列中元素 型態是迭代器 e.g "example good a  "
        result=''

        for i in reverse: #整理反轉後的格式 去掉空的字串 
            
            if not i == '':
                result += i
                result  += " "

        return result[:-1]  #去掉尾的空格

