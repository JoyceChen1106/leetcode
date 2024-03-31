#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果 p 或 q 中有一個是 None，則返回 p 與 q 是否相等的結果。
        if p is None or q is None:
            return p == q
        
        # 如果 p 與 q 的值相等，且它們的左子樹和右子樹也相等，則返回 True。
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True
    
# @lc code=end

