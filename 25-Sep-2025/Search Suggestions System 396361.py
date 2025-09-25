# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        
        for ch in searchWord:
            prefix += ch
            suggestions = []
            for p in products:
                if p.startswith(prefix):
                    suggestions.append(p)
                if len(suggestions) == 3:
                    break
            res.append(suggestions)
        
        return res