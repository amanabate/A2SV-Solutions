# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1
        
        # Build adjacency lists
        graph = [defaultdict(list), defaultdict(list)]
        for u, v in redEdges:
            graph[RED][u].append(v)
        for u, v in blueEdges:
            graph[BLUE][u].append(v)

        # Distance array initialized to infinity
        res = [float('inf')] * n
        
        # Queue: (node, steps, color_of_prev_edge)
        queue = deque()
        queue.append((0, 0, RED))  # Starting with red
        queue.append((0, 0, BLUE))  # Starting with blue
        
        # Visited[node][color] to prevent revisiting
        visited = [[False] * 2 for _ in range(n)]
        visited[0][RED] = visited[0][BLUE] = True
        
        while queue:
            node, steps, color = queue.popleft()
            res[node] = min(res[node], steps)
            
            # Alternate color
            next_color = 1 - color
            for nei in graph[next_color][node]:
                if not visited[nei][next_color]:
                    visited[nei][next_color] = True
                    queue.append((nei, steps + 1, next_color))
        
        # Replace 'inf' with -1 where no path was found
        return [x if x != float('inf') else -1 for x in res]
