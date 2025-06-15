# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        a, b = edges[0]
        c, d = edges[1]

        # The common node between the two edges is the center
        if a == c or a == d:
            return a
        return b