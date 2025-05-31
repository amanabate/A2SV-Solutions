# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
           return []
    
        p_count = defaultdict(int)
        s_count = defaultdict(int)
        
       
        for i in range(len(p)):
            p_count[p[i]] += 1
            s_count[s[i]] += 1
        
        result = []

        if p_count == s_count:
            result.append(0)
        

        left = 0
        
        for right in range(len(p), len(s)):
            s_count[s[right]] += 1
            s_count[s[left]] -= 1

            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
           
            if s_count == p_count:
                result.append(left)
        
        return result