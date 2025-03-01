# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n = len(words)

        char_sets = [set(word) for word in words]   
        lengths = [len(word) for word in words]

        max_product = 0

        for i in range(n):
            for j in range(i + 1, n):
                if not (char_sets[i] & char_sets[j]):  
                    max_product = max(max_product, lengths[i] * lengths[j])

        return max_product
                