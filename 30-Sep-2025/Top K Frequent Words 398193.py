# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        # Sort by (-frequency, word) so highest freq first, then lexicographically
        sorted_words = sorted(count.keys(), key=lambda w: (-count[w], w))
        return sorted_words[:k]