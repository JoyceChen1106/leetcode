#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
       

        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        st = ""
        # 我們迭代字典中的項目，按值（字符的頻率）升序排序
        for i in sorted(dic.items(), key=lambda x: x[1]):
            # 將字符根據其頻率進行重複添加
            st += i[0] * i[1]
        # 因為排序是升序的，所以我們需要將結果字串反轉以得到降序的頻率排列
        return st[::-1]

# @lc code=end

