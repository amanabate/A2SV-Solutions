# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

from collections import deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_graph = [[] for _ in range(n)]
        outdegree = [0] * n

        for u in range(n):
            for v in graph[u]:
                rev_graph[v].append(u)
            outdegree[u] = len(graph[u])

        q = deque([i for i in range(n) if outdegree[i] == 0])
        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True
            for nei in rev_graph[node]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    q.append(nei)

        return [i for i in range(n) if safe[i]]