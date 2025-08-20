# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for r in range(1, n):
            for c in range(n):
                best = matrix[r-1][c]
                if c > 0:
                    best = min(best, matrix[r-1][c-1])
                if c < n-1:
                    best = min(best, matrix[r-1][c+1])
                matrix[r][c] += best
        
        return min(matrix[-1])