# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            if len(path) >= 4:
                return

            for length in range(1, 4):  # part can be 1, 2, or 3 digits
                if start + length > len(s):
                    break
                part = s[start:start+length]
                # skip invalid: leading zero or >255
                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue
                backtrack(start+length, path + [part])

        backtrack(0, [])
        return res