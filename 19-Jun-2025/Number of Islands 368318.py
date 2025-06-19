# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return
            grid[row][col] = '0'  # mark as visited
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)

        return islands
