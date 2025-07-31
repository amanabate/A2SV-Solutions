# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) == (m - 1, n - 1):
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = dp(i + 1, j) + dp(i, j + 1)
            
            return memo[(i, j)]

        return dp(0, 0)