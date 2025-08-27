# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        diff = xor & -xor
        a = b = 0
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n
        return [a, b]