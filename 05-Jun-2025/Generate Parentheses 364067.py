# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        stack = [("", 0, 0)]  

        while stack:
            current, open_c, close_c = stack.pop()

            if len(current) == 2 * n:
                result.append(current)
                continue

            if open_c < n:
                stack.append((current + "(", open_c + 1, close_c))

            if close_c < open_c:
                stack.append((current + ")", open_c, close_c + 1))

        return result