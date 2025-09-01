# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Step 1: process all "=="
        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])
        
        # Step 2: check all "!="
        for eq in equations:
            if eq[1:3] == "!=":
                if find(eq[0]) == find(eq[3]):
                    return False
        
        return True