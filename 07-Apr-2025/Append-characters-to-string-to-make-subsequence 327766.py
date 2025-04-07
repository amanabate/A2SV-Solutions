# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        if len(t) == 1 and t in s:
            return 0

        index_s = 0
        index_t = 0

        while index_s < len(s) and index_t < len(t):
            if s[index_s] == t[index_t]:
                index_t += 1
        
            index_s += 1

        return len(t) - index_t



