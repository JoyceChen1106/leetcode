#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:

        s_list = s.split(" ")
        reverse_list = []  # 创建一个空列表来存储反转后的单词
        for i in range(len(s_list)):
            reverse_list.append(s_list[len(s_list) - i - 1])
        return " ".join(reverse_list).strip()

