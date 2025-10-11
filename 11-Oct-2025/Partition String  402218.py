# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        curr = ""

        for ch in s:
            curr += ch
            if curr not in seen:
                res.append(curr)
                seen.add(curr)
                curr = ""
        return res