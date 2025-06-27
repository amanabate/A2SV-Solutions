# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = set()

        for from_node, to_node in edges:
            indegree.add(to_node)

        result = []
        
        for node in range(n):
            if node not in indegree:
                result.append(node)

        return result
