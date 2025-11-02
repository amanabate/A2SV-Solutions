# Problem: Count Unguarded Cells in the Grid - https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]  
        # 0 = empty, 1 = guard, 2 = wall, 3 = guarded
        
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 1 and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0: 
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
        
        return ans
