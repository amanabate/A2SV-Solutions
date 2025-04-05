# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        total = 0
        min_abs = float('inf')
        negative_count = 0
        
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                val = matrix[i][j]
                total += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs = min(min_abs, abs(val))
                j += 1
            i += 1

        if negative_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
            