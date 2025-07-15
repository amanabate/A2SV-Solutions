# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for _ in range(n)] 

        cols = set()     
        diag1 = set()   
        diag2 = set()    

        def backtrack(r):
            if r == n:
                result.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in diag1 or (r - c) in diag2:
                    continue  

                board[r][c] = 'Q'
                cols.add(c)
                diag1.add(r + c)
                diag2.add(r - c)

        
                backtrack(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)

        backtrack(0)
        return result