# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top_row = 0
        bottom_row = len(matrix) - 1

        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2

            if matrix[middle_row][0] < target and matrix[middle_row][-1] > target:
                break
            elif matrix[middle_row][0] > target:
                bottom_row = middle_row - 1
            else:
                top_row = middle_row + 1
        
        target_row = (top_row + bottom_row) // 2

        left_col = 0
        right_col = len(matrix[target_row]) - 1

        while left_col <= right_col:
            middle_col = (left_col + right_col) // 2

            if matrix[target_row][middle_col] == target:
                return True
            elif matrix[target_row][middle_col] > target:
                right_col = middle_col - 1
            else:
                left_col = middle_col + 1
        
        return False