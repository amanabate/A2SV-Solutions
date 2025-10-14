# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1

        # keep repeating until length >= b
        while len(repeated) < len(b):
            repeated += a
            count += 1

        # check if b is a substring
        if b in repeated:
            return count
        # try one more repeat (for overlap case)
        if b in repeated + a:
            return count + 1

        return -1