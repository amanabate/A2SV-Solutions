# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        Stack = []
        dict_brackets = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in dict_brackets:
                if Stack and Stack[-1] == dict_brackets[c]:
                   Stack.pop()
                else:
                    return False
            else:
                Stack.append(c)

        if not Stack:
            return True
        else:
            return False

