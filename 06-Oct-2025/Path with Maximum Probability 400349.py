# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        
        heap = [(-1.0, start_node)]  # (negative probability, node)
        
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob  # convert back to positive
            
            if node == end_node:
                return prob
            
            for nei, edgeProb in graph[node]:
                newProb = prob * edgeProb
                if newProb > maxProb[nei]:
                    maxProb[nei] = newProb
                    heapq.heappush(heap, (-newProb, nei))
        
        return 0.0
