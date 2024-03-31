#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 定義一個名為 Solution 的類別

        # 初始化最大長度 (maxlen) 和最大出現次數 (largestCount) 為 0
        maxlen, largestCount = 0, 0
        # 創建一個計數器字典 arr 來追蹤每個字元的出現次數
        arr = collections.Counter()
        
        # 逐一處理字串 s 中的每個字元
        for idx in range(len(s)):
            # 增加該字元在計數器中的出現次數
            arr[s[idx]] += 1
            # 更新最大出現次數 (largestCount) 為目前最大值
            largestCount = max(largestCount, arrs[idx])
            
            # 如果目前最大長度 (maxlen) 減去最大出現次數 (largestCount) 大於等於 k
            if maxlen - largestCount >= k:
                # 減少最左邊字元的出現次數，模擬移動窗口
                arr[s[idx - maxlen]] -= 1
            else:
                # 否則，增加最大長度 (maxlen)
                maxlen += 1
        
        # 返回最終的最大長度
        return maxlen

# @lc code=end

