#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        # 创建一个临时指针 temp，用于遍历链表
        temp = head
        
        # 初始化变量 s 用于计算链表的节点数
        s = 0
        
        # 遍歷整个個linklist，同時計算節點數
        while temp:
            s += 1
            temp = temp.next
        
        # 計算要删除的節點位置（倒数第 n 个節點）
        n = s - n
        
        # 將 temp 重新設置為表的頭節點
        temp = head
        
        # 如果要删除的是第一个節點，返回头節點的下一个節點
        if n == 0:
            return head.next
        
        # 遍历linklist，找到要删除節點的前一个節點（第 n-1 个節點）
        for i in range(n - 1):
            temp = temp.next
        
        # 如果要删除的節點的下一个節點存在，删除該節點
        if temp.next:
            temp.next = temp.next.next
        
        # 返回原始Link list的頭節點
        return head
 
# @lc code=end

