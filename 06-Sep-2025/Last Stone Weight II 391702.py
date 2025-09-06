# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [False] * (total + 1)
        dp[0] = True
        
        for stone in stones:
            for i in range(total, stone - 1, -1):
                if dp[i - stone]:
                    dp[i] = True
        
        for s in range(total // 2, -1, -1):
            if dp[s]:
                return total - 2 * s
        
        return 0
