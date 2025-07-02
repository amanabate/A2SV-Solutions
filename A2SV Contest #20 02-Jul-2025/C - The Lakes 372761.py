# Problem: C - The Lakes - https://codeforces.com/gym/618729/problem/C

import sys
input = sys.stdin.readline

t = int(input())
directions = [(1,0), (-1,0), (0,1), (0,-1)]

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    max_volume = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                stack = [(i,j)]
                volume = 0
                visited[i][j] = True
                
                while stack:
                    x, y = stack.pop()
                    volume += grid[x][y]
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if grid[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                
                if volume > max_volume:
                    max_volume = volume
    
    print(max_volume)
