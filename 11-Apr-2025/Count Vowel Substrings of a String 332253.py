# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        result = 0
        n = len(word)
        substring_freqs = []
        vowels = set("aeiou")

        for i in range(n):
            for j in range(i + 1, n + 1):
                if j - i >= 5:
                    substring = word[i:j]
                    if all(c in vowels for c in substring):
                        count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
                        for char in substring:
                            if char in count:
                                count[char] += 1
                        
                        if count['a'] > 0 and count['e'] > 0 and count['i'] > 0 and count['o'] > 0 and count['u'] > 0:
                            result += 1

        return result