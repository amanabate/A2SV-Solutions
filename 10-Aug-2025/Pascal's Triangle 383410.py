# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for row in range(numRows):
            current_row = [1] * (row + 1)
            
            for j in range(1, row):
                current_row[j] = result[row - 1][j - 1] + result[row - 1][j]
            
            result.append(current_row)
        
        return result