# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [0] * n  # dp[i] = max profit up to day i
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[-1]