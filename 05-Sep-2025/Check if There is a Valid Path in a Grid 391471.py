# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Possible connections for each street type
        dirs = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)],      # right, up
        }
        
        # Opposite directions for checking valid connection
        opposite = {(0, -1):(0, 1), (0, 1):(0, -1),
                    (-1, 0):(1, 0), (1, 0):(-1, 0)}
        
        from collections import deque
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while q:
            x, y = q.popleft()
            if (x, y) == (m-1, n-1):
                return True
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if opposite[(dx, dy)] in dirs[grid[nx][ny]]:
                        visited.add((nx, ny))
                        q.append((nx, ny))
        
        return False