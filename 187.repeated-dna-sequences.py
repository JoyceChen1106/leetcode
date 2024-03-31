#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
    
        # 創建一個字典，用來追蹤已訪問的DNA序列
        visited = {}
        # 用於存儲重複的DNA序列
        res = []
        # 遍歷字串s中的每個字符，我們只需要檢查前面10個字符，所以範圍是len(s) - 9
        for i in range(len(s) - 9):
            # 從當前位置i開始，擷取10個字符長度的DNA序列
            sequence = s[i:i+10]
            # 檢查當前的DNA序列是否已經存在於visited字典中
            if sequence in visited:
                # 如果序列已經存在，進一步檢查它是否已經被確定為重複
                if not visited[sequence]:
                    # 如果還未標記為重複，則標記它為True，並將它添加到res列表中
                    visited[sequence] = True
                    res.append(sequence)
            else:
                # 如果序列不在visited中，將它加入visited，並將其值設為False，表示首次遇到這個序列
                visited[sequence] = False
        # 迴圈結束後，返回存儲重複DNA序列的res列表
        return res

        
# @lc code=end

