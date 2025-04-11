# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        if len(t) == 1 and t in s:
            return 0

        i = 0
        
        for char in s:
            if i < len(t) and char == t[i]:
                i += 1  # Move to the next character in t
        
        return len(t) - i