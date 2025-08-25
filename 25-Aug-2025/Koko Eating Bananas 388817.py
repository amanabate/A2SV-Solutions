# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours <= h:
                ans = mid
                right = mid - 1  
            else:
                left = mid + 1 
        
        return ans