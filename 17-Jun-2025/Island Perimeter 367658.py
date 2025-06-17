# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:  # top neighbor
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:  # left neighbor
                        perimeter -= 2
        return perimeter