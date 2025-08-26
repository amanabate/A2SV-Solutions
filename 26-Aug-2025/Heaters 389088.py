# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        i = 0
        ans = 0
        
        for h in houses:
            while i < len(heaters) - 1 and abs(heaters[i+1] - h) <= abs(heaters[i] - h):
                i += 1
            ans = max(ans, abs(heaters[i] - h))
        
        return ans