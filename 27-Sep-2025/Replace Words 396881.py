# Problem: Replace Words - https://leetcode.com/problems/replace-words/

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)  # check shorter roots first
        words = sentence.split()

        for i, word in enumerate(words):
            for root in dictionary:
                if word.startswith(root):
                    words[i] = root
                    break   # stop at the shortest root
        return " ".join(words)
