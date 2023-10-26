#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        # 如果輸入的串列 head 為空或者 k 為 0，則不需要進行旋轉，直接返回原串列
        if not head or k == 0:
            return head

        cur = head
        length = 0
        while cur:
            length += 1
            prev = cur
            cur = cur.next
        else:
            prev.next = head  # 將原始串列形成循環，將最後一個節點的 next 指向第一個節點

        k = length - (k % length)  # 計算實際需要向右旋轉的步數，以避免多餘的旋轉
        while k > 0:  # 進行 k 次向右旋轉（順時針）
            k -= 1
            prev = head
            head = head.next
        else:
            prev.next = None  # 斷開原始串列，使其成為新的尾部
            return head  # 返回旋轉後的串列的開頭

# @lc code=end

