# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
           return False
    
        rows, cols = len(board), len(board[0])
        
        def backtrack(i, j, index, visited):
            if index == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited or board[i][j] != word[index]:
                return False
            
            visited.add((i, j))
            res = (backtrack(i + 1, j, index + 1, visited) or
                backtrack(i - 1, j, index + 1, visited) or
                backtrack(i, j + 1, index + 1, visited) or
                backtrack(i, j - 1, index + 1, visited))
            visited.remove((i, j))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0, set()):
                        return True
        return False