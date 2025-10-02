# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Min-heap: (time, node)
        heap = [(0, k)]
        
        # Record shortest time to each node
        dist = {}
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:  # already processed
                continue
            dist[node] = time
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + wt, nei))
        
        if len(dist) == n:
            return max(dist.values())
        return -1