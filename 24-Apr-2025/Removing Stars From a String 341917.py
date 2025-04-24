# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:

        Stack = []
        n = len(s)

        for i in range(n):
            if s[i] == '*':
                if Stack:
                    Stack.pop()
            else:
                Stack.append(s[i])
        return ''.join(Stack)
                    
            

        