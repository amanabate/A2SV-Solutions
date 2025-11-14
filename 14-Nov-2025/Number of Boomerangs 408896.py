# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        
        for i in points:
            distance_count = {}
            for j in points:
                if i == j:
                    continue
                    
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                d = dx*dx + dy*dy
                distance_count[d] = distance_count.get(d, 0) + 1
            
            for val in distance_count.values():
                count += val * (val - 1)
        
        return count