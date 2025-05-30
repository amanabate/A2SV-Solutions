# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}
    
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
    
        return -1