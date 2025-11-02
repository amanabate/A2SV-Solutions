# Problem: Replace Words - https://leetcode.com/problems/replace-words/

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()

        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        # Find shortest root for a word
        def findRoot(word):
            node = root
            prefix = []
            for ch in word:
                if ch not in node.children:
                    return word
                prefix.append(ch)
                node = node.children[ch]
                if node.is_end:
                    return "".join(prefix)
            return word

        return " ".join(findRoot(w) for w in sentence.split())