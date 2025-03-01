# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        row_index = 0

        for i, row in enumerate(mat):
            ones_count = sum(row)
            if ones_count > max_ones:
                max_ones = ones_count
                row_index = i

        return [row_index, max_ones]
        