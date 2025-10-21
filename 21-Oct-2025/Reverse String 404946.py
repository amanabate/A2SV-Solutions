# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack = []
        for strg in s:
            stack.append(strg)
        for strg in range(len(s)):
            s[strg] = stack.pop()
        return s