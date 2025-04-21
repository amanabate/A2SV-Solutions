# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffled_string = [""] * len(s)
        for i in range(len(s)):
             shuffled_string[indices[i]] = s[i]
        return ''.join(shuffled_string)