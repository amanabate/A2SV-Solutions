# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1
