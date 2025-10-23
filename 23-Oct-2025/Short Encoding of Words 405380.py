# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            for i in range(1, len(word)):
                words_set.discard(word[i:])
                
        return sum(len(word) + 1 for word in words_set)