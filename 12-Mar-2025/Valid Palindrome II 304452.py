# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
            

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                without_left = s[left + 1 : right + 1]
                without_right = s[left : right]
                
                return is_palindrome(without_left) or is_palindrome(without_right)

            left += 1
            right -= 1

        return True
