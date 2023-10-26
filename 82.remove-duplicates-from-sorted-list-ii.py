#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        
        c = Counter(temp)
        print(c)
        temp = [k for k, v in c.items() if v == 1]

        # 創建一個虛擬節點(dummy)和當前節點(cur)
        dummy = cur = ListNode()
        
        for i in temp:
            # 創建一個新的節點，將其值設定為 i
            cur.next = ListNode(i)
            cur = cur.next
        
        # 返回虛擬節點(dummy)的下一個節點，即處理後的串列的開頭
        return dummy.next

# @lc code=end

