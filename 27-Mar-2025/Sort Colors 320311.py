# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        size = len(nums)
        
        for i in range(size):
            min_idx = i

            for j in range(i + 1, size):
                if nums[j] < nums[min_idx]:  
                    min_idx = j

            nums[i], nums[min_idx] = nums[min_idx], nums[i]  

