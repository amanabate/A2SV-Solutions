# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()

        arrows = 1
        # Start with the end of the first balloon
        current_end = points[0][1]

        for xstart, xend in points[1:]:
            # No overlap, need new arrow
            if xstart > current_end:
                arrows += 1
                current_end = xend
            else:
                # Overlap, update current_end to be the minimum
                current_end = min(current_end, xend)

        return arrows