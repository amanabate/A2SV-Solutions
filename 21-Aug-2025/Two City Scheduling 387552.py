# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by difference (bCost - aCost)
        costs.sort(key=lambda x: x[1] - x[0])
        
        n = len(costs) // 2
        total = 0
        
        # First n people → City B, rest → City A
        for i in range(n):
            total += costs[i][1]  # send to B
        for i in range(n, 2 * n):
            total += costs[i][0]  # send to A
        
        return total