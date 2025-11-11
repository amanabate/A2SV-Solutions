# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
            def match(query, pattern):
                i = 0  # pointer for pattern
                for ch in query:
                    if i < len(pattern) and ch == pattern[i]:
                        i += 1
                    elif ch.isupper():
                        return False
                return i == len(pattern)

            return [match(q, pattern) for q in queries]