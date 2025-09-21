# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        maze[entrance[0]][entrance[1]] = "+"  # mark entrance as visited
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            r, c, steps = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                    if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:  
                        return steps + 1  # found nearest exit
                    maze[nr][nc] = "+"  # mark as visited
                    q.append((nr, nc, steps + 1))
        
        return -1