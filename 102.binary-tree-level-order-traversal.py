#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # 初始化一個使用deque數據結構的隊列，並將根節點添加到其中。
        Q = deque([root])

        # 創建一個列表來存儲二叉樹的層級。使用根節點的值來初始化它。
        levels = [[root.val]]

        # 創建一個臨時的deque來存儲下一層的節點。
        temp = deque()

        # 開始一個while循環，以逐層遍歷二叉樹。
        while Q:
            # 從隊列中取出前端的節點。
            node = Q.popleft()

            # 檢查當前節點是否有左子節點，並將其添加到臨時隊列中。
            if node.left:
                temp.append(node.left)

            # 檢查當前節點是否有右子節點，並將其添加到臨時隊列中。
            if node.right:
                temp.append(node.right)

            # 如果當前層級已完全處理完成，則將下一層級的節點添加到levels列表中，並重新設置隊列和臨時隊列。
            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()

        return levels

# @lc code=end

