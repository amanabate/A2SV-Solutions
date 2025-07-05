# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        n = len(words)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            is_valid = words[i][0] in vowels and words[i][-1] in vowels
            prefix[i + 1] = prefix[i] + (1 if is_valid else 0)
        
        result = []
        for li, ri in queries:
            result.append(prefix[ri + 1] - prefix[li])
        
        return result
