# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            temp = []

            if d < n:
                row = 0
                col = d
            else:
                row = d - n + 1
                col = n - 1

            while row < m and col >= 0:
                temp.append(mat[row][col])
                row += 1
                col -= 1

            if d % 2 == 0:
                temp.reverse()

            result.extend(temp)

        return result