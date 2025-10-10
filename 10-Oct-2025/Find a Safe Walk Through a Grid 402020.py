# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, health - grid[0][0])])
        visited = {(0, 0): health - grid[0][0]}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            x, y, h = queue.popleft()
            
            if h <= 0:
                continue
            
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    # Only visit if we have more health than previously at this cell
                    if nh > 0 and visited.get((nx, ny), -1) < nh:
                        visited[(nx, ny)] = nh
                        queue.append((nx, ny, nh))
        
        return False