# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Create DP array and initialize all values to infinity
        dp = [float('inf')] * (amount + 1)

        
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        
        return -1 if dp[amount] == float('inf') else dp[amount]
