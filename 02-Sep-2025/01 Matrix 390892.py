# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        
        # Step 1: Initialize queue with all 0s and mark 1s as -1 (unvisited)
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1   # mark unvisited 1
        
        # Step 2: BFS
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1:
                    mat[ni][nj] = mat[i][j] + 1
                    q.append((ni, nj))
        
        return mat