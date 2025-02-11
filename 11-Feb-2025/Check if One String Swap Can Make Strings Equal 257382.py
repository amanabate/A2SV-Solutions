# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        index = []
        if s1 == s2:
            return True
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                index.append(i)

            if len(index) > 2:
                return False

        if len(index) == 2:
            i, j = index
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            else:
                return False

        return False