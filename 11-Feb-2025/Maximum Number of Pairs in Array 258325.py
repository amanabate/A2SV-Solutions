# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        pair_integers = 0
        leftover_integers = 0
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for freq in count.values():
            pair_integers += freq // 2 
            leftover_integers += freq % 2  
        
        return [pair_integers, leftover_integers]