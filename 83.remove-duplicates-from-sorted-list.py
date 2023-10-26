#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
 # 定義單鏈結串列節點的類別
# 每個節點包含一個數值(val)和指向下一個節點的指針(next)



        # 初始化一個指標cur，從串列的開頭（head）開始
        cur = head
        
        # 當當前節點（cur）存在且下一個節點也存在時
        while cur and cur.next:
            # 如果當前節點的值等於下一個節點的值，表示重複
            if cur.val == cur.next.val:
                # 將下一個節點的指針指向下下個節點，跳過下一個節點，等於刪除了重複元素
                cur.next = cur.next.next
            else:
                # 如果當前節點和下一個節點的值不相等，則繼續向下遍歷
                cur = cur.next

        # 回傳處理後的串列的開頭
        return head

# @lc code=end

