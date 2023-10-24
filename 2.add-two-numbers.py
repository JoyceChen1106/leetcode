#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
 
    # Solution 類別包含一個方法 addTwoNumbers，用於將兩個鏈結串列相加。
    # 它接收兩個鏈結串列 (l1 和 l2) 作為輸入，並返回一個新的鏈結串列。
    
            # 初始化進位(carry)為 0
            carry = 0
            # 創建虛擬節點(dummy)，它作為結果鏈結的起點
            dummy = ListNode()
            curr = dummy
            while l1 != None or l2 != None:
                # 如果 l1 鏈結還有節點，將節點值加到 carry
                if l1 != None:
                    carry += l1.val
                    l1 = l1.next
                # 如果 l2 鏈結還有節點，將節點值加到 carry
                if l2 != None:
                    carry += l2.val
                    l2 = l2.next
                # 創建一個新節點，值為 carry 的個位數
                curr.next = ListNode(carry % 10)
                # 計算進位
                carry = 1 if carry >= 10 else 0
                # 將 curr 指針移到下一個節點
                curr = curr.next
            # 如果最後還有進位，創建一個額外的節點
            if carry != 0:
                curr.next = ListNode(carry)
            # 返回虛擬節點(dummy)之後的節點，即結果鏈結的起點
            return dummy.next

# @lc code=end

