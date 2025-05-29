# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/



class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def countLiveNeighbors(r, c):
            live = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or j < 0 or i >= m or j >= n:
                        continue
                    live += board[i][j] & 1
            return live

        for i in range(m):
            for j in range(n):
                live_neighbors = countLiveNeighbors(i, j)
                if board[i][j] & 1:  
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[i][j] |= 2  
                else:  
                    if live_neighbors == 3:
                        board[i][j] |= 2  

    
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  
