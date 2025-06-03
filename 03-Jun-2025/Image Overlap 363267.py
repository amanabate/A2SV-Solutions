# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
    
    
        ones1 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
        
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    ones2.append((i, j))

    
        vector_count = Counter()

        for (x1, y1) in ones1:
            for (x2, y2) in ones2:
                dx = x2 - x1
                dy = y2 - y1
                
                vector_count[(dx, dy)] += 1
        
        if vector_count:
            return max(vector_count.values())
        else:
            return 0