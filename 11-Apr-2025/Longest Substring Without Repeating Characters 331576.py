# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     
        longest_str = set()
        left = 0 
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in longest_str:
                longest_str.remove(s[left])
                left += 1  
    
            longest_str.add(s[right])
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
