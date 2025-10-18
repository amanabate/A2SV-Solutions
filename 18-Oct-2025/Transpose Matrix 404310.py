# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        # Create a new n x m matrix
        transposed = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        
        return transposed