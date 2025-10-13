# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        
        count = 0
        for word in words:
            prev = -1
            found = True
            for c in word:
                if c not in pos:
                    found = False
                    break
                i = bisect.bisect_right(pos[c], prev)
                if i == len(pos[c]):
                    found = False
                    break
                prev = pos[c][i]
            if found:
                count += 1
        return count