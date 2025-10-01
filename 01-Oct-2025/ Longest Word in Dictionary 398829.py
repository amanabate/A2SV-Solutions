# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  # sort to ensure lexicographical order
        built = set([""])  
        longest = ""
        
        for word in words:
            if word[:-1] in built:  # check if prefix exists
                built.add(word)
                if len(word) > len(longest):  
                    longest = word
        return longest