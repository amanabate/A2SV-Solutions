# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        transposed_matrix = []
        size = range(len(matrix[0]))

        for i in size:
            new = []
            for num in matrix:
                new.append(num[i])
                
            transposed_matrix.append(new)

        return transposed_matrix
