# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        left = 0
        right = len(height) - 1 
        for _ in range(len(height) - 1):
            cur_hght = min(height[left], height[right])
            w = right - left 
            cur_area = cur_hght * w

            max_area = max(max_area , cur_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
              
        