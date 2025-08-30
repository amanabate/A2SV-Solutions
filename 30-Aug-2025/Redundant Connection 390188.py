# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parent[pv] = pu
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]