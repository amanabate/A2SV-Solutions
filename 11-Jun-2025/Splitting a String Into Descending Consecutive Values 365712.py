# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        
        n = len(s)
        
        def dfs(index, prev_value):

            if index == n:
                return True
                
            for j in range(index + 1, n + 1):
                current_value = int(s[index:j])

                if current_value == prev_value - 1:
                    if dfs(j, current_value):
                        return True
          
                if current_value >= prev_value:
                    break

            return False
        
       
        for i in range(1, n):
            first_value = int(s[:i])

            if dfs(i, first_value):
                return True

        return False