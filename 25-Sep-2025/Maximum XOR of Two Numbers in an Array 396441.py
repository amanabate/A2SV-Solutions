# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0
        
        for bit in range(31, -1, -1):  # 31 down to 0
            mask |= (1 << bit)
            prefixes = {num & mask for num in nums}
            candidate = res | (1 << bit)
            
            # check if two prefixes can achieve candidate
            if any((candidate ^ p) in prefixes for p in prefixes):
                res = candidate
        
        return res