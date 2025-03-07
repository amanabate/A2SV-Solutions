# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        list_s = list(s)
        for i in range(len(list_s)):
            list_s.append(list_s.pop(0)) 

            if ''.join(list_s) == goal:
                return True

        return False

        